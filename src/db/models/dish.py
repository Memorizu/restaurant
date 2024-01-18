from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models import SubMenu


class Dish(Base):
    name: Mapped[str] = mapped_column(String(30), unique=True)
    price: Mapped[float | None] = mapped_column(Float(precision=2))
    submenu_id: Mapped[int] = mapped_column(ForeignKey('submenus.id'))
    submenu: Mapped['SubMenu'] = relationship('SubMenu', back_populates='dishs', uselist=False)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __repr__(self):
        return str(self)
