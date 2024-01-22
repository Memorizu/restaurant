from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_helper import db_helper
from src.db.models import Menu, SubMenu
from api_v1.submenu import crud


async def submenu_by_id(
        menu_id: Annotated[int, Path],
        submenu_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> SubMenu:
    return await crud.get_submenu(session=session, menu_id=menu_id, submenu_id=submenu_id)
