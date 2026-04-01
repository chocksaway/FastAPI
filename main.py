import asyncio
import json
from typing import AsyncIterator

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import StreamingResponse

from learn.phrase import Phrase, TranslatedPhrase


class HealthResponse(BaseModel):
    status: str


class PalindromeResponse(BaseModel):
    text: str
    translation: str | None = None
    is_palindrome: bool


app = FastAPI(title="Learn API")


@app.get("/", tags=["meta"])
def root() -> dict[str, str]:
    return {"message": "Learn API is running"}


@app.get("/health", tags=["meta"])
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/palindrome", tags=["phrases"])
def palindrome(text: str, translation: str | None = None) -> PalindromeResponse:
    phrase = TranslatedPhrase(text, translation) if translation else Phrase(text)
    return PalindromeResponse(
        text=text,
        translation=translation,
        is_palindrome=phrase.is_palindrome(),
    )

async def process_items() -> AsyncIterator[str]:
    # Example streaming generator: simulate processing 10 items
    for i in range(1, 100000):
        # Simulate async work (I/O, CPU offload, DB, etc.)
        await asyncio.sleep(0.5)
        result = {"item": i, "status": "processed"}
        # Send newline-delimited JSON so clients can parse incrementally
        yield json.dumps(result) + "\n"



@app.get("/stream")
async def stream_get(request: Request):
    async def event_stream():
        async for chunk in process_items():
            # If client disconnects, stop processing
            if await request.is_disconnected():
                break
            yield chunk.encode("utf-8")
    return StreamingResponse(event_stream(), media_type="application/x-ndjson")
