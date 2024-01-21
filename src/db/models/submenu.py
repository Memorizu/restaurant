from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


if TYPE_CHECKING:
    from src.db.models import Dish
    from src.db.models import Menu


class SubMenu(Base):
    __tablename__ = 'submenus'
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey('menus.id'))
    menu: Mapped['Menu'] = relationship('Menu', back_populates='submenus', uselist=False)
    dishes: Mapped[list['Dish']] = relationship('Dish', back_populates="submenu", lazy='selectin', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.title}'

    def __repr__(self):
        return str(self)
