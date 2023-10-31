from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Routes
@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    from models.restaurant import Restaurant
    from models.pizza import Pizza
    from models.restaurantPizza import RestaurantPizza

    # Your implementation for the function

@app.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    from models.restaurant import Restaurant
    from models.pizza import Pizza
    from models.restaurantPizza import RestaurantPizza

    # Your implementation for the function

@app.route("/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    from models.restaurant import Restaurant
    from models.pizza import Pizza
    from models.restaurantPizza import RestaurantPizza

    # Your implementation for the function

@app.route("/pizzas", methods=["GET"])
def get_pizzas():
    from models.pizza import Pizza

    # Your implementation for the function

@app.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    from models.pizza import Pizza

    # Your implementation for the function

if __name__ == "__main__":
    app.run(debug=True)
