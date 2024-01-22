from fastapi.exceptions import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status

from api_v1.submenu.schemas import SubMenuCreateSchema, SubMenuUpdateSchema
from src.db.models import SubMenu, Menu


async def get_submenus(menu_id: int, session: AsyncSession) -> list[SubMenu]:
    stmt = (select(SubMenu).
            join(Menu).
            filter(SubMenu.menu_id == menu_id).
            options(selectinload(SubMenu.dishes)).
            order_by(SubMenu.id))
    result: Result = await session.execute(stmt)
    submenus = result.scalars().all()
    return list(submenus)


async def get_submenu(session: AsyncSession, menu_id: int, submenu_id: int) -> SubMenu:
    stmt = (select(SubMenu).
            join(Menu).
            filter(SubMenu.menu_id == menu_id).
            filter(SubMenu.id == submenu_id).
            options(selectinload(SubMenu.dishes)).
            order_by(SubMenu.id)
            )
    result: Result = await session.execute(stmt)
    submenu = result.scalar_one_or_none()
    if not submenu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='submenu not found'
        )
    return submenu


async def create_submenu(session: AsyncSession, submenu: SubMenuCreateSchema, menu: Menu) -> SubMenu:
    submenu = SubMenu(
        menu_id=menu.id,
        title=submenu.title,
        description=submenu.description
    )
    session.add(submenu)
    await session.commit()
    await session.refresh(submenu)
    return submenu


async def update_submenu(
        session: AsyncSession,
        submenu: SubMenu,
        submenu_update: SubMenuUpdateSchema
) -> SubMenu:
    for name, value in submenu_update.model_dump().items():
        setattr(submenu, name, value)
    await session.commit()
    await session.refresh(submenu)
    return submenu


async def delete_submenu(
        session: AsyncSession,
        submenu: SubMenu,
) -> None:
    await session.delete(submenu)
    await session.commit()
