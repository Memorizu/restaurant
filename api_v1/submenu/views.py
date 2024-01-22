from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.submenu.dependencies import submenu_by_id
from api_v1.submenu.schemas import SubMenuSchema, SubMenuCreateSchema, SubMenuUpdateSchema
from src.db.db_helper import db_helper
from api_v1.submenu import crud
from src.db.models import Menu, SubMenu


router = APIRouter(tags=['submenus'])


@router.get('/', response_model=list[SubMenuSchema], status_code=200)
async def get_submenus(
        menu_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_submenus(session=session, menu_id=menu_id)


@router.get('/{submenu_id}', response_model=SubMenuSchema, status_code=200)
async def get_submenu(
        menu_id: int,
        submenu_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_submenu(session=session, menu_id=menu_id, submenu_id=submenu_id)


@router.post('/', response_model=SubMenuSchema, status_code=201)
async def create_menu(
        submenu: SubMenuCreateSchema,
        menu: Menu = Depends(submenu_by_id),
        session: AsyncSession = Depends(db_helper.get_scoped_session),
):
    return await crud.create_submenu(session=session, submenu=submenu, menu=menu)


@router.patch('/{submenu_id}', response_model=SubMenuSchema, status_code=200)
async def update_submenu(
        submenu_update: SubMenuUpdateSchema,
        submenu: SubMenu = Depends(submenu_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_submenu(
        session=session,
        submenu=submenu,
        submenu_update=submenu_update
    )


@router.delete('/{submenu_id}', status_code=204)
async def delete_submenu(
        submenu: SubMenu = Depends(submenu_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_submenu(session=session, submenu=submenu)
