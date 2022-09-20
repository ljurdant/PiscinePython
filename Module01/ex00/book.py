import datetime
from recipe import Recipe 
class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {
            "starter" : [],
            "lunch" : [],
            "dessert": []
        }
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError("Name attribute must be a string")
        self._name = value
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list.values():
            for recipe in recipe_type:
                if recipe.name == name:
                    print(str(recipe)+"\n")
                    return (recipe)
        raise AttributeError("There is no recipe by the name of",name)
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipes_list:
            raise AttributeError("recipe type")
        if not len(self.recipes_list[recipe_type]):
            print("There are no recipes of type:",recipe_type)
        else:
            return ([recipe for recipe in self.recipes_list[recipe_type]])
            # print(", ".join([recipe.name for recipe in self.recipes_list[recipe_type]]))

        
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            raise ValueError("Type passed must be a Recipe class")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
    

