from datetime import date
from pydantic import BaseModel, ConfigDict


class OrderResponse(BaseModel):
    id: int
    product_name: str
    quantity: int
    unit_price: float
    order_date: date

    model_config = ConfigDict(from_attributes=True)


class CustomerResponse(BaseModel):
    id: int
    first_name: str
    surname: str
    email: str
    status: str
    created_at: date
    orders: list[OrderResponse]

    model_config = ConfigDict(from_attributes=True)