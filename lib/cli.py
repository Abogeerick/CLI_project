import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, Category, Supplier, Transaction  # Import your database models

DATABASE_URL = "sqlite:///inventory.db"  # Update with your database URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def list_products():
    """List all products in the inventory."""
    products = session.query(Product).all()
    for product in products:
        click.echo(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

@cli.command()
@click.option('--name', prompt='Product Name', help='Name of the product')
@click.option('--description', help='Description of the product')
@click.option('--quantity', type=int, help='Quantity of the product')
@click.option('--price', type=float, help='Price of the product')
@click.option('--supplier_id', type=int, help='Supplier ID')
@click.option('--category_id', type=int, help='Category ID')
def add_product(name, description, quantity, price, supplier_id, category_id):
    """Add a new product to the inventory."""
    product = Product(
        name=name,
        description=description,
        quantity=quantity,
        price=price,
        supplier_id=supplier_id,
        category_id=category_id
    )
    session.add(product)
    session.commit()
    click.echo("Product added successfully.")

@cli.command()
@click.argument('product_id', type=int)
def view_product(product_id):
    """View details of a specific product."""
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        click.echo(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")
    else:
        click.echo("Product not found.")

@cli.command()
def list_categories():
    """List all product categories."""
    categories = session.query(Category).all()
    for category in categories:
        click.echo(f"ID: {category.id}, Name: {category.name}")

@cli.command()
@click.option('--name', prompt='Category Name', help='Name of the category')
def add_category(name):
    """Add a new product category."""
    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo("Category added successfully.")

@cli.command()
def list_suppliers():
    """List all suppliers."""
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        click.echo(f"ID: {supplier.id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}")

@cli.command()
@click.option('--name', prompt='Supplier Name', help='Name of the supplier')
@click.option('--contact_info', help='Contact information for the supplier')
def add_supplier(name, contact_info):
    """Add a new supplier."""
    supplier = Supplier(name=name, contact_info=contact_info)
    session.add(supplier)
    session.commit()
    click.echo("Supplier added successfully.")

@cli.command()
def list_transactions():
    """List all transactions."""
    transactions = session.query(Transaction).all()
    for transaction in transactions:
        click.echo(f"ID: {transaction.id}, Product ID: {transaction.product_id}, Type: {transaction.transaction_type}, Quantity Changed: {transaction.quantity_changed}, Date: {transaction.transaction_date}")

@cli.command()
@click.option('--product_id', type=int, prompt='Product ID', help='ID of the product involved in the transaction')
@click.option('--transaction_type', prompt='Transaction Type', help='Type of the transaction (e.g., purchase, sale)')
@click.option('--quantity_changed', type=int, prompt='Quantity Changed', help='Quantity change in the transaction')
@click.option('--transaction_date', prompt='Transaction Date', help='Date of the transaction')
@click.option('--notes', help='Additional notes for the transaction')
def add_transaction(product_id, transaction_type, quantity_changed, transaction_date, notes):
    """Add a new transaction."""
    transaction = Transaction(
        product_id=product_id,
        transaction_type=transaction_type,
        quantity_changed=quantity_changed,
        transaction_date=transaction_date,
        notes=notes
    )
    session.add(transaction)
    session.commit()
    click.echo("Transaction added successfully.")

if __name__ == '__main__':
    cli()
