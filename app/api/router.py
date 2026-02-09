from fastapi import APIRouter

from app.modules.auth.router import router as auth_router
from app.modules.comments.router import router as comments_router


router = APIRouter(
    prefix="/api",
)

router.include_router(auth_router)
router.include_router(comments_router)