import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, Category, Supplier, Transaction
from faker import Faker

# Define your SQLite database URL here
DATABASE_URL = "sqlite:///products.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

# Define the database models (ensure they are defined in the 'models.py' file)
from models import Product, Category, Supplier, Transaction

# Clear existing data from tables
session.query(Category).delete()
session.query(Supplier).delete()
session.query(Product).delete()
session.query(Transaction).delete()
session.commit()

# Generate data for categories table
for _ in range(50):
    category = Category(name=fake.word())
    session.add(category)

# Generate data for suppliers table
for _ in range(50):
    supplier = Supplier(name=fake.company(), contact_info=fake.email())
    session.add(supplier)

# Generate data for products table
for _ in range(50):
    product = Product(
        name=fake.catch_phrase(),
        description=fake.paragraph(),
        quantity=random.randint(1, 100),
        price=round(random.uniform(10.0, 500.0), 2),
        supplier_id=random.randint(1, 50),  # Assuming you have 50 suppliers
        category_id=random.randint(1, 50)   # Assuming you have 50 categories
    )
    session.add(product)

# Generate data for transactions table
for _ in range(50):
    transaction = Transaction(
        product_id=random.randint(1, 50),        # Assuming you have 50 products
        transaction_type=random.choice(["Purchase", "Sale"]),
        quantity_changed=random.randint(1, 50),
        transaction_date=fake.date_this_decade(),
        notes=fake.sentence()
    )
    session.add(transaction)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
