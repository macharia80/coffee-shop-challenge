from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
steve = Customer("Steve")
dima = Customer("Dima")

# Create some coffees
mocha = Coffee("Mocha")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create some orders
order1 = Order(steve, mocha, 2.0)
order2 = Order(steve, latte, 3.0)
order3 = Order(dima, mocha, 4.0)

# Test relationships
print(f"Steve's orders: {[o.coffee.name for o in steve.orders()]}")
print(f"Steve's coffees: {[c.name for c in steve.coffees()]}")
print(f"Mocha's customers: {[c.name for c in mocha.customers()]}")
print(f"Mocha's number of orders: {mocha.num_orders()}")
print(f"Mocha's average price: {mocha.average_price()}")

# Test bonus method
top_customer = Customer.most_aficionado(mocha)
print(f"Biggest mocha fan: {top_customer.name if top_customer else 'None'}")