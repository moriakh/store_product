class Product:

    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)
        return self

    def print_info(self):
        print(f'Product Name: {self.name}; ID: {self.id}; Category: {self.category}; Price: ${self.price}')
        return self