from fastapi import FastAPI
from pydantic import BaseModel

from phrase import Phrase, TranslatedPhrase


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
