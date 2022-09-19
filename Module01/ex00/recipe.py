
class Recipe:
    def __init__(self, name:str, cooking_lvl: int, cooking_time:int, ingredients:list,  description:str = "", recipe_type:str = ""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    def typeValidator(value, attribute, type):
        if type(value) != type:
            raise ValueError(attribute,"attribute must be a",type)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError("Name attribute must be a string")
        self._name = value

    @property
    def cooking_lvl(self):
        return self._cooking_lvl
    @cooking_lvl.setter
    def cooking_lvl(self, value):
        if type(value) != int:
            raise ValueError("Cooking level must be an int")
        elif value < 1 or value > 5:
            raise ValueError("Cooking level must be a number between 1 and 5 included")
        self._cooking_lvl = value
    
    @property
    def cooking_time(self):
        return self._cooking_time
    @cooking_time.setter
    def cooking_time(self, value):
        if type(value) != int:
            raise ValueError("Cooking time must be an int")
        elif value < 0:
            raise ValueError("Cooking time must be a non-negative number")
        self._cooking_time = value
    
    @property
    def ingredients(self):
        return self._ingredients
    @ingredients.setter
    def ingredients(self, value):
        if type(value) !=  list:
            raise ValueError("Ingredients must be a list")
        if not len(value):
            raise ValueError("Ingredients cannot be empty")
        self._ingredients = value
    
    @property
    def recipe_type(self):
        return self._recipe_type
    @recipe_type.setter
    def recipe_type(self, value):
        recipe_types = ["starter", "lunch", "dessert"]
        if type(value) != str:
            raise ValueError("Recipe type must be a string")
        elif value not in recipe_types:
            raise ValueError("Recipe type must be one of "+str(recipe_types))
        self._recipe_type = value
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        if type(value) != str:
            raise ValueError("Description must be a string")
        self._description = value


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = f"Name: {self.name}\nCooking level: {self.cooking_lvl}\nCooking time: {self.cooking_time} minutes\nIngredients: {self.ingredients}\nRecipe type: {self.recipe_type}\nDescription:{self.description}"
        return txt

# cake = Recipe("cake", 1, 5, ["flour", "chocolate", "milk", "egss"], "dessert", "A nice cake to eat with your friends")
# to_print = str(cake)
# print(to_print)