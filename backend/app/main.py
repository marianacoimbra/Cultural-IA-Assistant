from fastapi import FastAPI
from api.health import router as health_router
from api.profile import router as profile_router
from api.recommendations import router as recommendations_router

app = FastAPI()

app.include_router(health_router)
app.include_router(profile_router)
app.include_router(recommendations_router)