from book import Book
from recipe import Recipe

mybook = Book("Mybook")
cake = Recipe("chocolate cake", 1, 5, ["flour", "chocolate", "milk", "eggs"], "A nicer cake to eat with your friends", "dessert")
cake2 = Recipe("strawberry cake", 1, 5, ["flour", "strawberry", "milk", "eggs"], "A nice cake to eat with your friends", "dessert")

# cake2 = Recipe("sandwich", 0, 5, ["ham", "bread", "cheese"], "Simply good", "lunch")
# cake2 = Recipe("sandwich", '0', 5, ["ham", "bread", "cheese"], "Simply good", "lunch")
# cake2 = Recipe("sandwich", 1, 5, [], "Simply good", "lunch")

print("creation date: ",mybook.creation_date)
print("last update: ", mybook.last_update)

mybook.add_recipe(cake)
mybook.add_recipe(cake2)
mybook.get_recipe_by_name("strawberry cake")
print(mybook.get_recipes_by_types("dessert")[0])
# mybook.get_recipes_by_types("s")

print("last update: ", mybook.last_update)