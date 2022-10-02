from classes.product import Product

class Store:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return self
    
    def sell_product(self, cart):
        for id in cart:
            for product in self.products:
                if product.id == id:
                    self.products.remove(product)
        return self
    
    def print_products(self):
        print(f"UPDATED {self.name.upper()} ITEM LIST:")
        for product in self.products:
            product.print_info()
        print("\n\n\n")
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self