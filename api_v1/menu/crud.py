from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .schemas import MenuCreateSchema, MenuUpdateSchema
from src.db.models import Menu


async def get_menus(session: AsyncSession) -> list[Menu]:
    stmt = select(Menu).options(selectinload(Menu.submenus)).order_by(Menu.id)
    result: Result = await session.execute(stmt)
    menus = result.scalars().all()
    return list(menus)


async def get_menu(session: AsyncSession, menu_id: int) -> Menu | None:
    return await session.get(Menu, menu_id)


async def create_menu(session: AsyncSession, menu: MenuCreateSchema) -> Menu:
    menu = Menu(**menu.model_dump())
    session.add(menu)
    await session.commit()
    await session.refresh(menu)
    return menu


async def update_menu(
        session: AsyncSession,
        menu: Menu,
        menu_update: MenuUpdateSchema
) -> Menu:
    print(f'title {menu_update.title}\n description {menu_update.description}')
    for name, value in menu_update.model_dump().items():
        setattr(menu, name, value)
    print(f'title {menu_update.title}\n description {menu_update.description}')
    await session.commit()
    await session.refresh(menu)
    return menu


async def delete_menu(
        session: AsyncSession,
        menu: Menu,
) -> None:
    await session.delete(menu)
    await session.commit()
