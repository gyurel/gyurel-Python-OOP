class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name):
        for prd in self.products:
            if prd.name == product_name:
                self.products.remove(prd)

    def __repr__(self):
        info = ''
        for product in self.products:
            info += f"{product.name}: {product.quantity}\n"

        return info.strip()
