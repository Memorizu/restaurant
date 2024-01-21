from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.db.models.base import Base


if TYPE_CHECKING:
    from .submenu import SubMenu


class Menu(Base):
    __tablename__ = 'menus'
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    submenus: Mapped[list['SubMenu']] = relationship('SubMenu', back_populates='menu', lazy='selectin', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.title}'

    def __repr__(self):
        return str(self)
