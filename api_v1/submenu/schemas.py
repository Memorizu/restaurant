from pydantic import BaseModel, ConfigDict

from api_v1.dish.schemas import DishSchema


class SubMenuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str | None
    dishes: list[DishSchema] | None = None


class SubMenuCreateSchema(BaseModel):
    title: str
    description: str | None


class SubMenuUpdateSchema(SubMenuCreateSchema):
    pass
