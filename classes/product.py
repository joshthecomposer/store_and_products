import random

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = random.randint(1000, 10000)

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + percent_change
        if not is_increased:
            self.price -= (self.price * percent_change)
        return self
    
    def print_info(self):
        print("======================")
        print(f"Product: {self.name}\nPrice: ${self.price}\nCategory: {self.category}\nID: {self.id}")
        print("======================")
        return self
    
    def get_id(self):
        return self.id