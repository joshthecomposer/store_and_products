from classes.store import Store
from classes.product import Product

oven1 = Product("Oven 1", 39.99, "Storage & Utilities")
oven2 = Product("Oven 2", 39.99, "Storage & Utilities")
spoon1 = Product("Spoon 1", 3.00, "Kitchen Utensils")
spoon2 = Product("Spoon 2", 3.00, "Kitchen Utensils")
tv = Product("TV", 300, "Electronics")
playstation = Product("Playstation", 400, "Electronics")

walmart = Store("Walmart")

walmart.add_product(oven1).add_product(oven2).add_product(spoon1).add_product(spoon2).add_product(tv).add_product(playstation)

walmart.print_products()

item_1 = spoon1.get_id()
item_2 = spoon2.get_id()
item_3 = tv.get_id()

shopping_cart = [item_1, item_2, item_3]

walmart.sell_product(shopping_cart)

walmart.print_products()