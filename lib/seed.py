import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, Category, Supplier, Transaction

# Define your SQLite database URL here
DATABASE_URL = "sqlite:///products.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# List of sample product names and descriptions
product_names = ["Product A", "Product B", "Product C", "Product D", "Product E"]
descriptions = ["Description 1", "Description 2", "Description 3", "Description 4", "Description 5"]

# List of sample categories
categories = ["Category 1", "Category 2", "Category 3"]

# List of sample suppliers
suppliers = ["Supplier 1", "Supplier 2", "Supplier 3"]

# Seed the 'products' table with random data
for _ in range(50):
    product = Product(
        name=random.choice(product_names),
        description=random.choice(descriptions),
        quantity=random.randint(0, 100),  # Random quantity between 0 and 100
        price=round(random.uniform(10.0, 100.0), 2),  # Random price between 10.0 and 100.0 with 2 decimal places
        category=Category(name=random.choice(categories)),
        supplier=Supplier(name=random.choice(suppliers))
    )
    session.add(product)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
