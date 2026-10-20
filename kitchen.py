class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return (self.amount, self.unit) == (other.amount, other.unit)

    def __repr__(self):
        return f"{self.amount} {self.unit}"

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, converter, unit):
        return Quantity(self.amount / converter.rate(self.unit, unit), unit)

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


class Converter:
    def __init__(self):
        self.rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        if from_unit not in self.rates:
            self.rates[from_unit] = {}
        self.rates[from_unit][to_unit] = rate

    def rate(self, from_unit, to_unit):
        if from_unit == to_unit:
            return 1
        return self.rates[from_unit][to_unit]

    def reduce(self, source, unit):
        return source.reduce(self, unit)


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, converter, unit):
        left = converter.reduce(self.left, unit)
        right = converter.reduce(self.right, unit)
        return Quantity(left.amount + right.amount, unit)
