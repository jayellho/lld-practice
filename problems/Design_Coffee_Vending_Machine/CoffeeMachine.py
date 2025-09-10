from Inventory import Inventory
from Menu import Menu
from Coins import Coins

class CoffeeMachine:
    _instance = None
    def __init__(self):
        if CoffeeMachine._instance is not None:
            raise Exception(f"This should be a Singleton!")
        CoffeeMachine._instance = self
        self.menu = Menu()
        self.coins = Coins(100) # set default coins.
        self.inventory = Inventory()

    @staticmethod
    def get():
        if not CoffeeMachine._instance:
            CoffeeMachine()
        return CoffeeMachine._instance

    def display_menu(self):
        print(f"Current menu: {self.menu.coffees}")
    
    def _has_all_ingredients(self, recipe):
        for ingredient, qty in recipe.items():
            if ingredient not in self.inventory.ingredients or self.inventory.ingredients[ingredient] < qty:
                return False
        return True


    def buy_drink(self, selected_drink, payment):
        # no such drink.
        if selected_drink not in self.menu.coffees:
            raise Exception(f"{selected_drink} is not available. Choose another option.")
        
        
        found_drink = self.menu.coffees[selected_drink]

        # insufficient payment.
        if payment < self.menu.coffees[selected_drink].price:
            raise Exception(f"Insufficient payment of {payment}. Drink costs {found_drink.price}")
        

        # successfully dispensed:
        ## update change.
        change = self.coins.make_change(payment - found_drink.price)
        if change == -1:
            raise Exception(f"Unable to provide change for {payment}.")
        
        ## update inventory.
        self.inventory.update_inventory(found_drink.recipe)
        
        ## update menu.
        if not self._has_all_ingredients(found_drink.recipe):
            self.menu.remove_coffee(selected_drink)

        return change