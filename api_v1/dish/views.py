from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.dish.dependencies import dish_by_id
from api_v1.dish.schemas import DishSchema, DishCreateSchema, DishUpdateSchema
from api_v1.submenu.dependencies import submenu_by_id
from api_v1.submenu.schemas import SubMenuSchema
from src.db.db_helper import db_helper
from api_v1.dish import crud
from src.db.models import Menu, SubMenu, Dish


router = APIRouter(tags=['dishes'])


@router.get('/', response_model=list[DishSchema], status_code=200)
async def get_dishes(
        menu_id: int,
        submenu_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_dishes(session=session, menu_id=menu_id, submenu_id=submenu_id)


@router.get('/{dish_id}', response_model=SubMenuSchema, status_code=200)
async def get_dish(
        menu_id: int,
        submenu_id: int,
        dish_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_dish(session=session, menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)


@router.post('/', response_model=DishSchema, status_code=201)
async def create_dish(
        dish: DishCreateSchema,
        submenu: SubMenu = Depends(submenu_by_id),
        session: AsyncSession = Depends(db_helper.get_scoped_session),
):
    return await crud.create_dish(session=session, submenu=submenu, dish=dish)


@router.patch('/{dish_id}', response_model=DishSchema, status_code=200)
async def update_dish(
        dish_update: DishUpdateSchema,
        dish: Dish = Depends(dish_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_dish(
        session=session,
        dish=dish,
        dish_update=dish_update
    )


@router.delete('/{dish_id}', status_code=204)
async def delete_submenu(
        dish: Dish = Depends(dish_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_dish(session=session, dish=dish)
