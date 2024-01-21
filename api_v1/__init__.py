from fastapi import APIRouter

from .menu.views import router as menu_router


router = APIRouter()
router.include_router(router=menu_router, prefix='/menus')
