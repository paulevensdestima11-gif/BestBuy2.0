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
        Processes an order and returns the total price.

        Products added multiple times are combined into a
        single purchase before validation and pricing.

        Args:
            shopping_list (list):
                List of (Product, quantity) tuples.

        Returns:
            float:
                Total order cost.

        Raises:
            ValueError:
                If stock is insufficient or a purchase limit
                is exceeded.
        """
        aggregated = {}

        # Combine duplicate products
        for product, quantity in shopping_list:
            if product in aggregated:
                aggregated[product] += quantity
            else:
                aggregated[product] = quantity

        # Validate the entire order first
        for product, quantity in aggregated.items():

            if (
                    isinstance(product, products.LimitedProduct)
                    and quantity > product.get_maximum()
            ):
                raise ValueError(
                    f"Cannot buy more than "
                    f"{product.get_maximum()} "
                    f"of {product._name}."
                )

            if (
                    not isinstance(product, products.NonStockedProduct)
                    and quantity > product.get_quantity()
            ):
                raise ValueError(
                    f"Not enough stock for "
                    f"{product._name}."
                )

        total_price = 0

        # Process purchases after validation
        for product, quantity in aggregated.items():
            total_price += product.buy(quantity)

        return total_price

