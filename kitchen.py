# kitchen.py
CONVERSION_RATES = {
    ("oz", "g"): 28.35,
    ("g", "oz"): 1 / 28.35,
}


class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit):
        if self.unit == unit:
            return self
        rate = CONVERSION_RATES[(self.unit, unit)]
        return Quantity(self.amount * rate, unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit):
        left_reduced = self.left.reduce(unit)
        right_reduced = self.right.reduce(unit)
        return Quantity(left_reduced.amount + right_reduced.amount, unit)

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

class Converter:
    def reduce(self, quantity, unit):
        return quantity.reduce(unit)