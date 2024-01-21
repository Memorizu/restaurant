from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base

if TYPE_CHECKING:
    from src.db.models import SubMenu


class Dish(Base):
    __tablename__ = 'dishes'
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    price: Mapped[float | None] = mapped_column(Float(precision=2))
    submenu_id: Mapped[int] = mapped_column(ForeignKey('submenus.id'))
    submenu: Mapped['SubMenu'] = relationship('SubMenu', back_populates='dishes', uselist=False)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.title}'

    def __repr__(self):
        return str(self)
