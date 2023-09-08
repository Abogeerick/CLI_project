# Inventory Management CLI

This is an interactive Command-Line Interface (CLI) application for managing an inventory system. It allows you to perform various operations such as adding, viewing, and deleting products, categories, suppliers, and transactions in your inventory.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive**: All commands are interactive, making it easy to input data and manage your inventory.
- **CRUD Operations**: Supports Create, Read, Update, and Delete operations for products, categories, suppliers, and transactions.
- **View Details**: You can view detailed information about products and transactions.
- **List Data**: Lists all products, categories, suppliers, and transactions in your inventory.
- **Data Validation**: Provides data validation for numeric input (e.g., quantity, price).
- **Database**: Uses a SQLite database to persist inventory data.
- **Easy Setup**: Easy to set up and run, no complex configurations required.

## Installation

1. Clone the repository to your local machine:
```bash 
        git clone https://github.com/Abogeerick/CLI_project
```
2. Navigate to the project directory:
```bash 
    cd CLI_project
```
3. Activate virtual environment
```bash 
    pipenv install
```
## Usage
To run the CLI application, use the following command from the project directory:
```bash
    python3 cli.py
```
This will start the CLI, and you can then use the available commands to manage your inventory.

## Commands

The CLI provides the following commands:

    list_products: List all products in the inventory.
    add_product: Add a new product to the inventory interactively.
    view_product: View details of a specific product interactively.
    list_categories: List all product categories.
    add_category: Add a new product category interactively.
    delete_category: Delete an existing category from the inventory interactively.
    list_suppliers: List all suppliers.
    add_supplier: Add a new supplier interactively.
    delete_supplier: Delete an existing supplier from the inventory interactively.
    list_transactions: List all transactions.
    add_transaction: Add a new transaction interactively.
    delete_transaction: Delete an existing transaction from the inventory interactively.
    update_product: Update an existing product in the inventory interactively.

## Database
The CLI uses an SQLite database named products.db to store inventory data. You can find the database file in the project directory. You can also modify the DATABASE_URL variable in the cli.py file to specify a different database location or use a different database management system.

## Contributing
Contributions are welcome! If you have suggestions or want to report issues, please create a GitHub issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.