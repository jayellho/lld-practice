from Coffee import Coffee

class Menu:
    def __init__(self):
        self.coffees = {} # menu of available coffees
    

    def add_coffee(self, coffee: Coffee):
        if coffee.name in self.coffees:
            raise Exception(f"There is already {coffee.name} in the menu!")
        
        self.coffees[coffee.name] = coffee
    
    def remove_coffee(self, coffee: Coffee):
        if coffee.name not in self.coffees:
            raise Exception(f"{coffee.name} is not in the menu. Cannot be removed.")
        del self.coffees[coffee.name]
