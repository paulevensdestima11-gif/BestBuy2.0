class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Please enter a Name")
        self._name = name

        if price <= 0:
            raise ValueError("Please enter a valid number")
        self._price = price

        if quantity < 0:
            raise ValueError("Please enter a valid number ")
        self._quantity = quantity

        self._active = True

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

    def show(self):
        return (f"{self._name}, Price: {self._price}, Quantity: {self._quantity}")

    def buy(self, quantity):
        if quantity <= 0 or quantity > self._quantity:
            raise ValueError("Not enough product")

        self.set_quantity(self._quantity - quantity)

        return self._price * quantity








