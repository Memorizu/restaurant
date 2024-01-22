from pydantic import BaseModel, ConfigDict

from api_v1.submenu.schemas import SubMenuSchema


class MenuCreateSchema(BaseModel):
    title: str
    description: str


class MenuUpdateSchema(MenuCreateSchema):
    pass


class MenuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    submenus: list[SubMenuSchema] | None = None

