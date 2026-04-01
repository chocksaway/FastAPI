import asyncio
import json
import logging
import httpx
from celery import Celery

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# Configure a Celery client instance (same broker)
celery = Celery(broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")
# Reference the task by name; ensure worker imports tasks.py or is started appropriately.

STREAM_URL = "http://127.0.0.1:8000/stream"
CONCURRENCY = 10  # max concurrent task submissions

async def submit_to_celery(item: dict):
    logger.debug("Pushing to Redis → task=process_item payload=%s", json.dumps(item))
    result = celery.send_task("process_item", args=[item])
    logger.info("Task queued → id=%s payload=%s", result.id, json.dumps(item))

async def handle_stream():
    semaphore = asyncio.Semaphore(CONCURRENCY)
    logger.info("Connecting to stream: %s", STREAM_URL)
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", STREAM_URL) as resp:
            resp.raise_for_status()
            logger.info("Stream connected (HTTP %s)", resp.status_code)
            async for line in resp.aiter_lines():
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    logger.warning("Skipping non-JSON line: %r", line)
                    continue
                logger.debug("Received JSON from stream: %s", json.dumps(obj))
                # throttle concurrent submissions
                await semaphore.acquire()
                asyncio.create_task(worker_submit(obj, semaphore))

async def worker_submit(item, semaphore):
    try:
        await submit_to_celery(item)
    except Exception:
        logger.exception("Failed to submit item to Celery: %s", json.dumps(item))
    finally:
        semaphore.release()

if __name__ == "__main__":
    asyncio.run(handle_stream())
