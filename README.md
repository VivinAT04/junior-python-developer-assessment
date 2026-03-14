# Junior Python Developer Assessment

This project implements a small data processing and API system as part of the Junior Python/AWS Developer selection task.

The system includes:

- A repeatable database setup script
- A REST API for retrieving customer and order information
- A data extraction and transformation script that exports results to CSV

# Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

These technologies were chosen to keep the solution simple, lightweight, and easy to run locally while still following modern Python development practices.

# Project Structure

junior-python-developer-assessment
│
├── app
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── data
│   ├── customers.csv
│   └── orders.csv
│
├── scripts
│   ├── init_db.py
│   └── export_active_customers.py
│
├── output
│   └── active_customers_orders.csv
│
├── requirements.txt
└── README.md

# Setup Instructions

Clone the repository and install dependencies.

python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt

# Database Setup

Run the database initialization script:

python scripts/init_db.py

This script:

- creates the SQLite database
- creates the required tables
- loads sample data from CSV files

The script is **repeatable**. Running it multiple times will not create duplicate records.

# Running the API

Start the FastAPI server:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive documentation:

http://127.0.0.1:8000/docs

# API Endpoint

### Get customer with orders

GET /customers/{customer_id}

Example:

GET /customers/1

Response:

{
"id": 1,
"first_name": "John",
"surname": "Smith",
"email": "john.smith@example.com",
"status": "active",
"created_at": "2026-01-05",
"orders": [...]
}

If the customer does not exist:

404 Customer not found

# Data Export Script

Run:

python scripts/export_active_customers.py

The script:

1. Extracts all **active customers**
2. Combines `first_name` and `surname` into a single `name`
3. Calculates `total_value = quantity × unit_price`
4. Exports results to:

output/active_customers_orders.csv

# Design Decisions

### SQLite

SQLite was chosen to keep the project lightweight and easy to run without additional infrastructure.

### FastAPI

FastAPI provides a modern, fast, and well-structured framework for building REST APIs with automatic documentation.

### SQLAlchemy

SQLAlchemy was used as the ORM to provide clear database models and relationships between customers and orders.

# Possible Improvements

The following improvements could be added in future:

- Unit tests using pytest
- Docker containerisation
- Logging and error monitoring
- Pagination and filtering for API endpoints
- Environment variable configuration
- CI/CD pipeline

# Summary

This project demonstrates:

- database design
- API development
- ETL data processing
- clean project structure
- repeatable scripts
