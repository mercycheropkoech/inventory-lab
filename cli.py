import requests

BASE_URL = "http://127.0.0.1:5000"

while True:
    print("\n===== Inventory Menu =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Find Product by Barcode")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        response = requests.get(f"{BASE_URL}/inventory")
        print(response.json())

    elif choice == "2":
        barcode = input("Barcode: ")
        name = input("Product Name: ")
        brand = input("Brand: ")
        ingredients = input("Ingredients: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        data = {
            "barcode": barcode,
            "product_name": name,
            "brand": brand,
            "ingredients": ingredients,
            "price": price,
            "stock": stock
        }

        response = requests.post(f"{BASE_URL}/inventory", json=data)
        print(response.json())

    elif choice == "3":
        item_id = input("Item ID: ")
        price = float(input("New Price: "))
        stock = int(input("New Stock: "))

        response = requests.patch(
            f"{BASE_URL}/inventory/{item_id}",
            json={
                "price": price,
                "stock": stock
            }
        )

        print(response.json())

    elif choice == "4":
        item_id = input("Item ID: ")

        response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

        print(response.json())

    elif choice == "5":
        barcode = input("Barcode: ")

        response = requests.get(f"{BASE_URL}/product/{barcode}")

        print(response.json())

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")