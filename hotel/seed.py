from app import app, db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurantPizza import RestaurantPizza

def seed_data():
    with app.app_context():
        db.create_all()

        # Sample data to simulate the database
        restaurants = [
            Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201"),
            Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019"),
        ]

        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            # Add more pizzas here
        ]

        # Add the data to the database
        for restaurant in restaurants:
            db.session.add(restaurant)
        db.session.commit()

        for pizza in pizzas:
            db.session.add(pizza)
        db.session.commit()

        restaurant_pizzas = [
            RestaurantPizza(restaurant_id=restaurants[0].id, pizza_id=pizzas[0].id),
            RestaurantPizza(restaurant_id=restaurants[0].id, pizza_id=pizzas[1].id),
            # Add more restaurant_pizzas here
        ]

        for restaurant_pizza in restaurant_pizzas:
            db.session.add(restaurant_pizza)

        # Commit changes
        db.session.commit()

if __name__ == '__main__':
    seed_data()
