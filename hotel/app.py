from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate the database
restaurants = [
    {"id": 1, "name": "Sottocasa NYC", "address": "298 Atlantic Ave, Brooklyn, NY 11201"},
    {"id": 2, "name": "PizzArte", "address": "69 W 55th St, New York, NY 10019"},
]

pizzas = [
    {"id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
    {"id": 2, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
]

restaurant_pizzas = []

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    return jsonify(restaurants)

@app.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant)
    return jsonify({"error": "Restaurant not found"}), 404

@app.route("/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    global restaurants
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurants = [r for r in restaurants if r["id"] != restaurant_id]
            return "", 204
    return jsonify({"error": "Restaurant not found"}), 404

@app.route("/pizzas", methods=["GET"])
def get_pizzas():
    return jsonify(pizzas)

@app.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if price and 1 <= price <= 30 and pizza_id and restaurant_id:
        for restaurant in restaurants:
            if restaurant["id"] == restaurant_id:
                for pizza in pizzas:
                    if pizza["id"] == pizza_id:
                        restaurant_pizzas.append({"price": price, "pizza": pizza, "restaurant": restaurant})
                        return jsonify(pizza), 201

    return jsonify({"errors": ["validation errors"]}), 400

if __name__ == "__main__":
    app.run(debug=True)
