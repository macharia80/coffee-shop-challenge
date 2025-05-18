# Coffee Shop Challenge

A Python implementation of a coffee shop domain with three models: Coffee, Customer, and Order, demonstrating object relationships and business logic.

## Project Structure
coffee-shop-challenge/
├── Pipfile
├── debug.py # Demo script to test functionality
├── coffee.py # Coffee model implementation
├── customer.py # Customer model implementation
├── order.py # Order model implementation
└── tests/ # Test files
├── customer_test.py
├── coffee_test.py
└── order_test.py


## Models

### Coffee
- Represents a coffee type with:
  - Name (string, min 3 chars, immutable)
  - Methods to track orders and customers
  - Statistics methods (total orders, average price)

### Customer
- Represents a coffee shop customer with:
  - Name (string, 1-15 chars)
  - Methods to track orders and coffees
  - Method to create new orders
  - Class method to find top spender for a coffee

### Order
- Represents a transaction with:
  - Customer (Customer instance)
  - Coffee (Coffee instance)
  - Price (float, 1.0-10.0, immutable)

## Features

- Object relationships (many-to-many between Coffee and Customer through Order)
- Type validation and immutability constraints
- Business logic methods (average price, most frequent customer, etc.)
- Comprehensive test suite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<macharia80>/coffee-shop-challenge.git
   cd coffee-shop-challenge
Set up the environment:

bash
pipenv install
pipenv shell
Usage
Run the demo script:

bash
python debug.py
Run tests:

bash
python -m pytest tests/
Example Output
Running debug.py will show:

Steve's orders: ['Mocha', 'Latte']
Steve's coffees: ['Mocha', 'Latte']
Mocha's customers: ['Steve', 'Dima']
Mocha's number of orders: 2
Mocha's average price: 3.0
Biggest mocha fan: Dima
Requirements
Python 3.8+

pytest (for testing)

Testing
The project includes unit tests for all models:

tests/coffee_test.py

tests/customer_test.py

tests/order_test.py

Run all tests with:

bash
python -m pytest tests/

This README includes:

1. Project overview
2. Directory structure
3. Model descriptions
4. Key features
5. Installation instructions
6. Usage examples
7. Testing information
8. Requirements

You can add this to your project by:

```bash
touch README.md
