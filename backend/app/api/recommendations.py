from fastapi import APIRouter
from utils.mock import get_mock_recommendations

router = APIRouter()

@router.get("/mock/recommendations")
async def get_mock_recommendations_route():       
    return get_mock_recommendations()