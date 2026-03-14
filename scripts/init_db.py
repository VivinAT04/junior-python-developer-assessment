import csv
import os
import sys
from datetime import datetime

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.db import Base, SessionLocal, engine
from app.models import Customer, Order


CUSTOMERS_CSV = "data/customers.csv"
ORDERS_CSV = "data/orders.csv"


def load_customers(session):
    with open(CUSTOMERS_CSV, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            existing_customer = session.query(Customer).filter_by(id=int(row["id"])).first()

            if existing_customer:
                continue

            customer = Customer(
                id=int(row["id"]),
                first_name=row["first_name"],
                surname=row["surname"],
                email=row["email"],
                status=row["status"],
                created_at=datetime.strptime(row["created_at"], "%Y-%m-%d").date()
            )
            session.add(customer)

    session.commit()


def load_orders(session):
    with open(ORDERS_CSV, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            existing_order = session.query(Order).filter_by(id=int(row["id"])).first()

            if existing_order:
                continue

            order = Order(
                id=int(row["id"]),
                customer_id=int(row["customer_id"]),
                product_name=row["product_name"],
                quantity=int(row["quantity"]),
                unit_price=float(row["unit_price"]),
                order_date=datetime.strptime(row["order_date"], "%Y-%m-%d").date()
            )
            session.add(order)

    session.commit()


def main():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    try:
        load_customers(session)
        load_orders(session)
        print("Database initialized successfully.")
    finally:
        session.close()


if __name__ == "__main__":
    main()