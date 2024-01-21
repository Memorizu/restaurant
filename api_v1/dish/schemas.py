from pydantic import BaseModel, ConfigDict


class DishSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str | None = None
    price: float
