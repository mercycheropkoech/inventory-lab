# Inventory Management System

## Description
A Flask REST API for managing inventory items with OpenFoodFacts API integration.

## Features

- View inventory
- Add products
- Update products
- Delete products
- Fetch product details from OpenFoodFacts
- CLI application
- Unit tests

## Installation

git clone <repository>

cd inventory-management-system-lab

pip install -r requirements.txt

python3 app.py

## API Endpoints

GET /inventory

GET /inventory/<id>

POST /inventory

PATCH /inventory/<id>

DELETE /inventory/<id>

GET /product/<barcode>

## Run CLI

python3 cli.py

## Run Tests

pytest