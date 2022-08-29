from book import Book
from recipe import Recipe

mybook = Book("Mybook")
cake = Recipe("chocolate cake", 1, 5, ["flour", "chocolate", "milk", "egss"], "dessert", "A nicer cake to eat with your friends")
cake2 = Recipe("strawberry cake", 1, 5, ["flour", "strawberry", "milk", "egss"], "dessert", "A nice cake to eat with your friends")

mybook.add_recipe(cake)
mybook.add_recipe(cake2)
mybook.get_recipe_by_name("strawberry cake")
mybook.get_recipes_by_types("dessert")