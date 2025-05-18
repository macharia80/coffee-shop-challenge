import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_has_name(self):
        customer = Customer("Steve")
        assert customer.name == "Steve"
        
    def test_name_is_valid(self):
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("This name is way too long")
        with pytest.raises(TypeError):
            Customer(1)
            
    def test_has_many_orders(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order1 = Order(customer, coffee, 2.0)
        order2 = Order(customer, coffee, 3.0)
        assert order1 in customer.orders()
        assert order2 in customer.orders()
        
    def test_has_many_coffees(self):
        customer = Customer("Steve")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Latte")
        Order(customer, coffee1, 2.0)
        Order(customer, coffee2, 3.0)
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()
        
    def test_create_order(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 2.0)
        assert order in Order.all
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 2.0