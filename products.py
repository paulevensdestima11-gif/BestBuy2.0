from abc import ABC, abstractmethod


"""
Product and promotion system for a store application.

Includes:
- Base Product class
- Specialized product types
- Promotion system using polymorphism
"""


class Product:
    """
    Represents a general product in the store.
    """

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Please enter a name.")

        if price <= 0:
            raise ValueError("Please enter a valid price.")

        if quantity < 0:
            raise ValueError("Please enter a valid quantity.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion = None

    def get_quantity(self):
        """Returns current stock quantity."""
        return self._quantity

    def set_quantity(self, quantity):
        """Sets product quantity and deactivates if zero."""
        self._quantity = quantity

        if self._quantity == 0:
            self.deactivate()

    def is_active(self):
        """Checks if product is active."""
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    def get_promotion(self):
        """Returns assigned promotion."""
        return self._promotion

    def set_promotion(self, promotion):
        """Assigns a promotion to the product."""
        self._promotion = promotion

    def show(self):
        """Returns formatted product information."""
        promo_name = self._promotion._name if self._promotion else "None"

        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            f"Quantity: {self._quantity}, "
            f"Promotion: {promo_name}"
        )

    def buy(self, quantity):
        """
        Buys a given quantity of product and returns total price.
        Applies promotion if available.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if quantity > self._quantity:
            raise ValueError("Not enough product in stock.")

        if self._promotion:
            total = self._promotion.apply_promotion(self, quantity)
        else:
            total = self._price * quantity

        self.set_quantity(self._quantity - quantity)

        return total


class NonStockedProduct(Product):
    """
    Product type that is not physically stocked.
    """

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Disabled for non-stocked products."""
        pass

    def buy(self, quantity):
        """
        Purchases a non-stocked product.

        Since the product is not stocked, no stock validation
        or quantity reduction is performed.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)

        return self._price * quantity

    def show(self):
        """Returns display string for non-stocked product."""
        promo_name = self._promotion._name if self._promotion else "None"

        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            f"Quantity: Unlimited, "
            f"Promotion: {promo_name}"
        )


class LimitedProduct(Product):
    """
    Product with a maximum quantity per order.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def get_maximum(self):
        """
        Returns the maximum quantity allowed per order.
        """
        return self._maximum

    def buy(self, quantity):
        """
        Ensures purchase does not exceed maximum limit.
        """
        if quantity > self._maximum:
            raise ValueError(
                f"Cannot buy more than {self._maximum} "
                f"of {self._name}."
            )

        return super().buy(quantity)

    def show(self):
        """
        Returns product info including max order limit.
        """
        promo_name = self._promotion._name if self._promotion else "None"

        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            f"Quantity: {self._quantity}, "
            f"Maximum per order: {self._maximum}, "
            f"Promotion: {promo_name}"
        )


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Calculates discounted price."""
        pass


class PercentDiscount(Promotion):
    """
    Percentage-based discount promotion.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity):
        return (
            product._price
            * quantity
            * (1 - self._percent / 100)
        )


class SecondHalfPrice(Promotion):
    """
    Second item in every pair is half price.
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        pairs = quantity // 2
        leftover = quantity % 2

        pair_cost = product._price + (product._price / 2)
        leftover_cost = leftover * product._price

        return (pairs * pair_cost) + leftover_cost


class ThirdOneFree(Promotion):
    """
    Every third item is free.
    """

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        groups = quantity // 3
        leftover = quantity % 3

        paid_items = (groups * 2) + leftover

        return paid_items * product._price