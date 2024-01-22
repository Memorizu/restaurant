from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_helper import db_helper
from src.db.models import SubMenu
from api_v1.dish import crud


async def dish_by_id(
        submenu_id: Annotated[int, Path],
        dish_id: Annotated[int, Path],
        menu_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> SubMenu:
    return await crud.get_dish(session=session, dish_id=dish_id, submenu_id=submenu_id, menu_id=menu_id)
