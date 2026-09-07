from fastapi import FastAPI
from api.health import router as health_router
from api.profile import router as profile_router
from api.events import router as events_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(health_router)
app.include_router(profile_router)
app.include_router(events_router)