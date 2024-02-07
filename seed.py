from app import app
from models import db, Pizza, Restaurant, RestaurantPizza
from faker import Faker
import random

fake = Faker()


def seed_data():
    with app.app_context():
        print("🗑️  Dropping all tables...")
        db.drop_all()
        print("🔧  Creating all tables...")
        db.create_all()

        # Seed Pizzas with updated names
        print("🍕 Seeding pizzas...")
        pizza_seeds = [
            {"name": "Spicy Italian", "ingredients": "Dough, Spicy Tomato Sauce, Mozzarella, Pepperoni, Jalapeños"},
            {"name": "Veggie Delight", "ingredients": "Whole Wheat Dough, Tomato Sauce, Mozzarella, Bell Peppers, Olives, Onions, Mushrooms"},
            {"name": "BBQ Feast", "ingredients": "Dough, BBQ Sauce, Chicken, Bacon, Red Onions, Cilantro"},
            {"name": "Seafood Special", "ingredients": "Dough, Tomato Sauce, Shrimp, Tuna, Capers, Arugula"},
            {"name": "Four Cheese", "ingredients": "Dough, Tomato Sauce, Mozzarella, Parmesan, Gorgonzola, Feta"},
            {"name": "Truffle Mushroom", "ingredients": "Dough, White Sauce, Mozzarella, Mushrooms, Truffle Oil"},
            {"name": "Buffalo Wing", "ingredients": "Dough, Buffalo Sauce, Chicken, Blue Cheese, Celery"},
            {"name": "Sweet and Sour", "ingredients": "Dough, Sweet and Sour Sauce, Ham, Pineapple, Pickled Jalapeños"},
            {"name": "Taco Pizza", "ingredients": "Dough, Salsa, Ground Beef, Lettuce, Tomato, Taco Chips, Sour Cream"},
            {"name": "Greek Style", "ingredients": "Dough, Olive Oil, Tomato, Feta, Olives, Red Onion, Cucumber"},
            {"name": "Chicken Alfredo", "ingredients": "Dough, Alfredo Sauce, Chicken, Bacon, Mozzarella, Parsley"},
            {"name": "Breakfast Bonanza", "ingredients": "Dough, Cream Sauce, Mozzarella, Bacon, Sausage, Eggs, Chives"}
        ]

        for pizza_data in pizza_seeds:
            pizza = Pizza(**pizza_data)
            db.session.add(pizza)
        db.session.commit()

        # Seed Restaurants
        print("🏠 Seeding restaurants...")
        for _ in range(20):
            restaurant = Restaurant(
                name=fake.company(),
                address=fake.address(),
            )
            db.session.add(restaurant)
        db.session.commit()

        # Add Pizzas to Restaurants
        print("🍽️  Adding pizzas to restaurants...")
        restaurant_ids = [restaurant.id for restaurant in Restaurant.query.all()]
        pizza_ids = [pizza.id for pizza in Pizza.query.all()]

        for restaurant_id in restaurant_ids:
            for _ in range(random.randint(2, 5)):  # Each restaurant gets 2-5 types of pizza
                restaurant_pizza = RestaurantPizza(
                    restaurant_id=restaurant_id,
                    pizza_id=random.choice(pizza_ids),
                    price=random.uniform(10, 30)  # Random price between $10 and $30
                )
                db.session.add(restaurant_pizza)
        db.session.commit()

        print("✅ Done seeding!")

if __name__ == '__main__':
    seed_data()
