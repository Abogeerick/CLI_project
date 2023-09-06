from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Define your SQLite database URL here
DATABASE_URL = "sqlite:///products.db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create the database tables (if not already created)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()