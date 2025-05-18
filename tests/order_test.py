import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_has_price(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 2.0)
        assert order.price == 2.0
        
    def test_price_is_valid(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.0)
        with pytest.raises(TypeError):
            Order(customer, coffee, "free")
            
    def test_has_customer(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 2.0)
        assert order.customer == customer
        
    def test_has_coffee(self):
        customer = Customer("Steve")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 2.0)
        assert order.coffee == coffee