from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cultural IA Assistant API", version="0.1.0")


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="backend")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Cultural IA Assistant API"}
