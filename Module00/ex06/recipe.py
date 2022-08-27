cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipes(cookbook):
    print("Recipes:",', '.join(str(key) for key in cookbook))

def print_recipe(recipe_name):
    details = cookbook[recipe_name]
    print("Recipe for "+recipe_name+":")
    print("\tIngredients list:", cookbook[recipe_name]["ingredients"])
    print("\tTo be eaten for", cookbook[recipe_name]["meal"])
    print("\tTakes",cookbook[recipe_name]["prep_time"],"minutes of cooking")

print_recipes(cookbook)
print_recipe("cake")