from app import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
