from fastapi import APIRouter

from .menu.views import router as menu_router
from .submenu.views import router as submenu_router
from .dish.views import router as dishes_router

router = APIRouter()

router.include_router(router=menu_router, prefix='/menus')

router.include_router(
    router=submenu_router,
    prefix='/menus/{menu_id}/submenus',
)

router.include_router(
    router=dishes_router,
    prefix='/menus/{menu_id}/submenus/{submenu_id}/dishes',
)
