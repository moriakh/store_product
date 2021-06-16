class Store:

    def __init__(self, name):
        self.name = name
        products = []
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, product):
        self.products.pop(product)
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearence(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self