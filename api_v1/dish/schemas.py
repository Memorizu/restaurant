from pydantic import BaseModel, ConfigDict


class DishSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str | None = None
    price: float


class DishCreateSchema(BaseModel):
    title: str
    description: str | None = None
    price: float


class DishUpdateSchema(DishCreateSchema):
    pass
