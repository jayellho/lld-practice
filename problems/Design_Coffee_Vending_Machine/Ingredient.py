class Ingredient:
    def __init__(self, name, quantity, low_threshold):
        self.name = name
        self.quantity = quantity
        self._low_threshold = low_threshold

