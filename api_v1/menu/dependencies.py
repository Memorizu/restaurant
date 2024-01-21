from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_helper import db_helper
from src.db.models import Menu
from . import crud


async def menu_by_id(
        menu_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Menu:
    menu = await crud.get_menu(session=session, menu_id=menu_id)
    if menu:
        return menu
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Menu with id={menu_id} does not exist'
    )
