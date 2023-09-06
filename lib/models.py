from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///inventory.db')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add any additional fields as needed

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    # Add any additional fields as needed

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='products')  # Define the relationship
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')  # Define the relationship

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    transaction_type = Column(String(20))
    quantity_changed = Column(Integer)
    transaction_date = Column(Date)
    notes = Column(String)
    # Add any additional fields as needed

Base.metadata.create_all(engine)
