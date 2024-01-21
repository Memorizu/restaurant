from pydantic import BaseModel, ConfigDict

from api_v1.dish.schemas import DishSchema


class SubMenuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: list[DishSchema] | None = None
