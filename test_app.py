import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200

def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200

def test_add_item(client):
    response = client.post("/inventory", json={
        "barcode": "123456",
        "product_name": "Milk",
        "brand": "Brookside",
        "ingredients": "Milk",
        "price": 150,
        "stock": 10
    })

    assert response.status_code == 201

def test_update_item(client):
    response = client.patch("/inventory/1", json={
        "price": 500
    })

    assert response.status_code == 200

def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200