import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product, Category, Supplier, Transaction

DATABASE_URL = "sqlite:///products.db"
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
def add_product():
    """Add a new product to the inventory interactively."""
    click.echo("Enter the details for the new product:")
    name = click.prompt("Product Name")
    description = click.prompt("Description", default="")
    quantity = click.prompt("Quantity", type=int, default=0)
    price = click.prompt("Price", type=float)
    supplier_id = click.prompt("Supplier ID", type=int)
    category_id = click.prompt("Category ID", type=int)

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
def view_product():
    """View details of a specific product interactively."""
    product_id = click.prompt("Enter the Product ID", type=int)
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
def add_category():
    """Add a new product category interactively."""
    name = click.prompt("Category Name")
    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo("Category added successfully.")

@cli.command()
def delete_category():
    """Delete an existing category from the inventory interactively."""
    category_id = click.prompt("Enter the Category ID to delete", type=int)
    category = session.query(Category).filter_by(id=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        click.echo("Category deleted successfully.")
    else:
        click.echo("Category not found.")

@cli.command()
def list_suppliers():
    """List all suppliers."""
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        click.echo(f"ID: {supplier.id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}")

@cli.command()
def add_supplier():
    """Add a new supplier interactively."""
    name = click.prompt("Supplier Name")
    contact_info = click.prompt("Contact Info", default="")
    supplier = Supplier(name=name, contact_info=contact_info)
    session.add(supplier)
    session.commit()
    click.echo("Supplier added successfully.")

@cli.command()
def delete_supplier():
    """Delete an existing supplier from the inventory interactively."""
    supplier_id = click.prompt("Enter the Supplier ID to delete", type=int)
    supplier = session.query(Supplier).filter_by(id=supplier_id).first()
    if supplier:
        session.delete(supplier)
        session.commit()
        click.echo("Supplier deleted successfully.")
    else:
        click.echo("Supplier not found.")

@cli.command()
def list_transactions():
    """List all transactions."""
    transactions = session.query(Transaction).all()
    for transaction in transactions:
        click.echo(f"ID: {transaction.id}, Product ID: {transaction.product_id}, Type: {transaction.transaction_type}, Quantity Changed: {transaction.quantity_changed}, Date: {transaction.transaction_date}")

@cli.command()
def add_transaction():
    """Add a new transaction interactively."""
    click.echo("Enter the details for the new transaction:")
    product_id = click.prompt("Product ID", type=int)
    transaction_type = click.prompt("Transaction Type")
    quantity_changed = click.prompt("Quantity Changed", type=int)
    transaction_date = click.prompt("Transaction Date")
    notes = click.prompt("Notes", default="")

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

@cli.command()
def delete_transaction():
    """Delete an existing transaction from the inventory interactively."""
    transaction_id = click.prompt("Enter the Transaction ID to delete", type=int)
    transaction = session.query(Transaction).filter_by(id=transaction_id).first()
    if transaction:
        session.delete(transaction)
        session.commit()
        click.echo("Transaction deleted successfully.")
    else:
        click.echo("Transaction not found.")

if __name__ == '__main__':
    cli()
