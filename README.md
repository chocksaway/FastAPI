# learn + FastAPI

This project includes a minimal FastAPI app built around the existing palindrome classes.

## Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Then open the interactive docs at `http://127.0.0.1:8000/docs`.

## Try endpoints

- Root: `http://127.0.0.1:8000/`
- Health check: `http://127.0.0.1:8000/health`
- Palindrome check: `http://127.0.0.1:8000/palindrome?text=racecar`
- With translation (uses `TranslatedPhrase`):
  `http://127.0.0.1:8000/palindrome?text=recognize&translation=reconocer`
