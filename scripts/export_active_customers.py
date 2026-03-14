import csv
import os
import sys

# Allow script to access project modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.db import SessionLocal
from app.models import Customer

OUTPUT_FILE = "output/active_customers_orders.csv"


def export_active_customers():
    session = SessionLocal()

    customers = (
        session.query(Customer)
        .filter(Customer.status == "active")
        .all()
    )

    rows = []

    for customer in customers:
        name = f"{customer.first_name} {customer.surname}"

        for order in customer.orders:
            total_value = order.quantity * order.unit_price

            rows.append({
                "customer_id": customer.id,
                "name": name,
                "email": customer.email,
                "product_name": order.product_name,
                "quantity": order.quantity,
                "unit_price": order.unit_price,
                "total_value": total_value
            })

    os.makedirs("output", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "customer_id",
            "name",
            "email",
            "product_name",
            "quantity",
            "unit_price",
            "total_value"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    session.close()

    print(f"Export complete. File saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    export_active_customers()