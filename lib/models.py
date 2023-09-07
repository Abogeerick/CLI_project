# models.py

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///products.db')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Define the relationship with products
    products = relationship('Product', back_populates='category')

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    
    # Define the relationship with products
    products = relationship('Product', back_populates='supplier')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    quantity = Column(Integer, default=0)
    price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    
    # Define the relationship with supplier
    supplier = relationship('Supplier', back_populates='products')
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Define the relationship with category
    category = relationship('Category', back_populates='products')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    transaction_type = Column(String(20))
    quantity_changed = Column(Integer)
    transaction_date = Column(Date)
    notes = Column(String)
