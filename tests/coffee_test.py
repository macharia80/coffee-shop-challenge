import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_has_name(self):
        coffee = Coffee("Mocha")
        assert coffee.name == "Mocha"
        
    def test_name_is_valid(self):
        with pytest.raises(ValueError):
            Coffee("ab")
        with pytest.raises(TypeError):
            Coffee(1)
            
    def test_has_many_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Steve")
        order1 = Order(customer, coffee, 2.0)
        order2 = Order(customer, coffee, 3.0)
        assert coffee in order1.coffee
        assert coffee in order2.coffee
        
    def test_has_many_customers(self):
        coffee = Coffee("Flat White")
        customer1 = Customer("Steve")
        customer2 = Customer("Dima")
        Order(customer1, coffee, 2.0)
        Order(customer2, coffee, 3.0)
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()
        
    def test_num_orders(self):
        coffee = Coffee("Espresso")
        assert coffee.num_orders() == 0
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        assert coffee.num_orders() == 1
        
    def test_average_price(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 4.0)
        assert coffee.average_price() == 3.0