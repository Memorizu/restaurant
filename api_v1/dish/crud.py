from fastapi.exceptions import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api_v1.dish.schemas import DishCreateSchema, DishUpdateSchema
from src.db.models import SubMenu, Menu, Dish


async def get_dishes(menu_id: int, submenu_id: int, session: AsyncSession) -> list[SubMenu]:
    stmt = (select(Dish).
            join(SubMenu).
            filter(Dish.submenu_id == submenu_id).
            filter(SubMenu.menu_id == menu_id).
            order_by(Dish.id))
    result: Result = await session.execute(stmt)
    dishes = result.scalars().all()
    return list(dishes)


async def get_dish(session: AsyncSession, menu_id: int, submenu_id: int, dish_id) -> SubMenu:
    stmt = (select(Dish).
            join(SubMenu).
            filter(Menu.id == menu_id).
            filter(Dish.submenu_id == submenu_id).
            filter(Dish.id == dish_id)
            )
    result: Result = await session.execute(stmt)
    dish = result.scalar_one_or_none()
    if not dish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='submenu not found'
        )
    return dish


async def create_dish(session: AsyncSession, dish: DishCreateSchema, submenu: SubMenu) -> Dish:
    dish = Dish(
        submenu_id=submenu.id,
        title=dish.title,
        description=dish.description,
        price=dish.price
    )
    session.add(dish)
    await session.commit()
    await session.refresh(dish)
    return dish


async def update_dish(
        session: AsyncSession,
        dish: Dish,
        dish_update: DishUpdateSchema
) -> Dish:
    for name, value in dish_update.model_dump().items():
        setattr(dish, name, value)
    await session.commit()
    await session.refresh(dish)
    return dish


async def delete_dish(
        session: AsyncSession,
        dish: Dish,
) -> None:
    await session.delete(dish)
    await session.commit()
