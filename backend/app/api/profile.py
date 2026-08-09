from fastapi import APIRouter
from utils.mock import get_mock_profile

router = APIRouter()

@router.get("/mock/profile")
async def get_mock_profile_route():
    return get_mock_profile()