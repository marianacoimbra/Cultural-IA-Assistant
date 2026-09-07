from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"message": "Everything is working fine, Mari! :)"}