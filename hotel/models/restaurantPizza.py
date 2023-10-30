from app import db

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, price, restaurant_id, pizza_id):
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id
