from pydantic import BaseModel, ConfigDict

from api_v1.submenu.schemas import SubMenuSchema


class MenuBaseSchema(BaseModel):
    name: str
    submenus: list[SubMenuSchema] | None = None


class MenuCreateSchema(BaseModel):
    title: str
    description: str


class MenuUpdateSchema(MenuCreateSchema):
    pass


class MenuPartialUpdateSchema(MenuBaseSchema):
    name: str | None = None
    submenus: list[SubMenuSchema] | None = None


class MenuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str | None = None
    submenus: list[SubMenuSchema] | None = None

