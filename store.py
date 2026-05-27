import products

class Store:
    def __init__(self, products):
        self._products = products

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self._products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        result = []
        for product in self._products:
            if product.is_active():
                result.append(product)
        return result

    def order(self, shopping_list):
        total = 0
        for product in shopping_list:
            product, quantity = product
            total += product.buy(quantity)
        return total


