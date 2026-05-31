"""
Store module for managing products and customer orders.
"""


import products


class Store:
    """
    Represents a store that holds and manages products.
    """

    def __init__(self, products):
        """
        Initializes the store with a list of products.

        Args:
            products (list): List of Product objects.
        """
        self._products = products

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): Product to add.
        """
        self._products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): Product to remove.
        """
        self._products.remove(product)

    def get_total_quantity(self):
        """
        Returns total quantity of all products in store.

        Returns:
            int: Total quantity.
        """
        total = 0

        for product in self._products:
            total += product.get_quantity()

        return total

    def get_all_products(self):
        """
        Returns a list of active products.

        Returns:
            list: Active Product objects.
        """
        active_products = []

        for product in self._products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        """
        Processes an order and returns total price.

        Args:
            shopping_list (list): List of (Product, quantity) tuples.

        Returns:
            float: Total order cost.
        """
        total_price = 0

        for item in shopping_list:
            product, quantity = item
            total_price += product.buy(quantity)

        return total_price