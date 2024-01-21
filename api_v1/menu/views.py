from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.menu.dependencies import menu_by_id
from src.db.db_helper import db_helper
from api_v1.menu import crud

from api_v1.menu.schemas import MenuSchema, MenuCreateSchema, MenuUpdateSchema
from src.db.models import Menu

router = APIRouter(tags=['menus'])


@router.get('/', response_model=list[MenuSchema], status_code=200)
async def get_menus(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_menus(session=session)


@router.get('/{menu_id}', response_model=MenuSchema, status_code=200)
async def get_menu(menu: MenuSchema = Depends(menu_by_id)):
    return menu


@router.post('/', response_model=MenuSchema, status_code=201)
async def create_menu(
        menu: MenuCreateSchema,
        session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    return await crud.create_menu(session=session, menu=menu)


@router.patch('/{menu_id}', response_model=MenuSchema, status_code=200)
async def update_menu(
        menu_update: MenuUpdateSchema,
        menu: Menu = Depends(menu_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_menu(
        session=session,
        menu=menu,
        menu_update=menu_update
    )


@router.delete('/{menu_id}', status_code=204)
async def delete_menu(
        menu: Menu = Depends(menu_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_menu(session=session, menu=menu)
