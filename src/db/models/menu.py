from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.db.models.base import Base


if TYPE_CHECKING:
    from .submenu import SubMenu


class Menu(Base):
    name: Mapped[str] = mapped_column(String(30), unique=True)
    submenus: Mapped[list['SubMenu']] = relationship('SubMenu', back_populates='menu', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __repr__(self):
        return str(self)
