from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.db import SessionLocal
from app.models import Customer
from app.schemas import CustomerResponse

app = FastAPI(title="Junior Python Developer Assessment API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "API is running"}


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = (
        db.query(Customer)
        .options(joinedload(Customer.orders))
        .filter(Customer.id == customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer