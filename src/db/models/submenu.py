from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


if TYPE_CHECKING:
    from src.db.models.dish import Dish


class SubMenu(Base):
    name: Mapped[str] = mapped_column(String(30), unique=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey('menu.id'))
    dishes: Mapped[list['Dish']] = relationship('Dish', back_populates="submenu", cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __repr__(self):
        return str(self)
