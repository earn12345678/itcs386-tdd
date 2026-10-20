class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return (self.amount, self.unit) == (other.amount, other.unit)

    def __repr__(self):
        return f"{self.amount} {self.unit}"

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")
