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

def print_recipes():
    print("Recipes:",', '.join(str(key) for key in cookbook))

def print_recipe(recipe_name):
	if recipe_name in cookbook:
		details = cookbook[recipe_name]
		print("Recipe for "+recipe_name+":")
		print("\tIngredients list:", cookbook[recipe_name]["ingredients"])
		print("\tTo be eaten for", cookbook[recipe_name]["meal"])
		print("\tTakes",cookbook[recipe_name]["prep_time"],"minutes of cooking")
	else:
		print("There is no recipe for",recipe_name,"in your cookbook")
def print_recipe_from_input():
	print("\nPlease enter a recipe name to get its details:")
	print_recipe(input())

def delete_recipe(recipe_name):
	if recipe_name in cookbook:
		cookbook.pop(recipe_name)
	else:
		print("There is no recipe for",recipe_name,"in your cookbook")
def delete_from_input():
	print("\nPlease enter a recipe name to delete:")
	delete_recipe(input())

def add_recipe():
	print("Enter a name:")
	name = input()
	print("Enter ingredients:")
	ingredients = []
	new = input()
	while new != "":
		ingredients.append(new)
		new = input()
	print("Enter a meal type:")
	meal = input()
	print("Enter a preparation time:")
	prep_time = input()
	while not prep_time.isnumeric():
		print("Please enter a numerical value:")
		prep_time = input()
	recipe = {
		"ingredients" : ingredients,
		"meal": meal,
		"prep_time": int(prep_time)
	}
	cookbook[name] = recipe

def print_options():
	print("List of available option:","1: Add a recipe","2: Delete a recipe","3: Print a recipe","4: Print the cookbook","5: Quit", sep="\n\t")

def select_option():
	options = ["1", "2", "3", "4", "5"]
	print("\nPlease select an option:")
	selection = input()
	while selection not in options:
		print("\nSorry, this option does not exist.")
		print_options()
		print("\nPlease select an option:")
		selection = input()
	return int(selection)

def exit_cookbook():
	print("\nCookbook closed. Goodbye !")

print("Welcome to the Python Cookbook !")
print_options()
option_actions = {
	1 : add_recipe,
	2 : delete_from_input,
	3 : print_recipe_from_input,
	4 : print_recipes,
	5 : exit_cookbook
}
option = 0
while option != 5:
	option = select_option()
	option_actions[option]()
