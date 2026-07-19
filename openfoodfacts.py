import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def get_product(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data["status"] == 0:
        return None

    product = data["product"]

    return {
        "barcode": barcode,
        "product_name": product.get("product_name", ""),
        "brand": product.get("brands", ""),
        "ingredients": product.get("ingredients_text", "")
    }