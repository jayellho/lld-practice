class Coins:
    def __init__(self, amount):
        self.amount = amount

    def make_change(self, requested_amount):
        if requested_amount > self.amount:
            return -1
        else:
            self.amount -= requested_amount
            return requested_amount