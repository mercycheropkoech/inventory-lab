from flask import Flask, jsonify, request
from inventory import inventory

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API is running!",
        "routes": [
            "GET /inventory",
            "GET /inventory/<id>",
            "POST /inventory",
            "PATCH /inventory/<id>",
            "DELETE /inventory/<id>"
        ]
    })

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"message": "Item not found"}), 404

    return jsonify(item), 200

@app.route("/inventory", methods=["POST"])
def add_item():

    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "barcode": data["barcode"],
        "product_name": data["product_name"],
        "brand": data["brand"],
        "ingredients": data["ingredients"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"message":"Item not found"}),404

    data = request.get_json()

    item.update(data)

    return jsonify(item),200

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    item = next((item for item in inventory if item["id"] == item_id), None)

    if item is None:
        return jsonify({"message":"Item not found"}),404

    inventory.remove(item)

    return jsonify({"message":"Item deleted"}),200

if __name__ == "__main__":
    app.run(debug=True)