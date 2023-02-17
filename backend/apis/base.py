from fastapi import APIRouter

from apis.routes import stats


api_router = APIRouter()

api_router.include_router(stats.router, prefix="/stats", tags=["Stats"])
