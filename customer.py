from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Must be a Coffee instance")
        
        customers = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customers:
                    customers[order.customer] += order.price
                else:
                    customers[order.customer] = order.price
        
        if not customers:
            return None
            
        return max(customers.items(), key=lambda item: item[1])[0]