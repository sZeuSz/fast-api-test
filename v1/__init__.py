from app.api.v1.app_router import router as app_router
from app.api.v1.user_router import router as user_router
from fastapi import APIRouter


router = APIRouter(prefix="/v1", tags=["API v1"])
router.include_router(app_router)
router.include_router(user_router, tags=["user"])