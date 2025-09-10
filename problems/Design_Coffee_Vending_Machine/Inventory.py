from Ingredient import Ingredient

class Inventory:
    def __init__(self):
        self.ingredients = {}
    
    def _notify(low_items):
        print(f"These items are low in stock: {low_items}")

    def update_inventory(self, recipe):
        low_items = []
        for ingredient, amount in recipe.items():
            self.ingredients[ingredient].quantity -= amount

            if self.ingredients[ingredient].quantity < self.ingredients[ingredient]._low_threshold:
                low_items.append(ingredient)
        
        if low_items:
            self._notify(low_items)


    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.name in self.ingredients:
            raise Exception(f"Ingredient {ingredient.name} already exists in inventory.")
        else:
            self.ingredients[ingredient.name] = ingredient
            if ingredient.quantity < ingredient._low_threshold:
                self._notify(ingredient.name)


