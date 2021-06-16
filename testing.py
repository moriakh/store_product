from stores import Store
from products import Product

oxxo = Store('Oxxo')
okmarket = Store('OK Market')

bread = Product('Bread', '1.5', 'Food', 0)
water = Product('Water', '1', 'Food', 1)
toilet_paper = Product('Bread', '1.5', 'Cleaning', 2)

oxxo.add_product(bread).add_product(water)
okmarket.add_product(water).add_product(toilet_paper)

bread.print_info()

for product in okmarket.products:
    print(product)

print()

okmarket.sell_product(water)

for product in okmarket.products:
    print(product)