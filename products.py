from abc import ABC, abstractmethod


class Product:
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
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

        if self._quantity == 0:
            self.deactivate()

    def is_active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def get_promotion(self):
        return self._promotion

    def set_promotion(self, promotion):
        self._promotion = promotion

    def show(self):
        promo_name = (
            self._promotion._name
            if self._promotion
            else "None"
        )

        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            f"Quantity: {self._quantity}, "
            f"Promotion: {promo_name}"
        )

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if quantity > self._quantity:
            raise ValueError("Not enough product in stock.")

        self.set_quantity(self._quantity - quantity)

        if self._promotion:
            return self._promotion.apply_promotion(
                self,
                quantity
            )

        return self._price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        pass

    def show(self):
        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            "Not stocked"
        )


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def buy(self, quantity):
        if quantity > self._maximum:
            raise ValueError(
                f"Cannot buy more than "
                f"{self._maximum} of {self._name}."
            )

        return super().buy(quantity)

    def show(self):
        return (
            f"{self._name}, "
            f"Price: {self._price}, "
            f"Quantity: {self._quantity}, "
            f"Maximum per order: {self._maximum}"
        )


class Promotion(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
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
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        pairs = quantity // 2
        leftover = quantity % 2

        pair_cost = (
            product._price
            + (product._price / 2)
        )

        leftover_cost = leftover * product._price

        return (pairs * pair_cost) + leftover_cost


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        groups = quantity // 3
        leftover = quantity % 3

        paid_items = (groups * 2) + leftover

        return paid_items * product._price