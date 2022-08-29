import random

def guess(n: int):
	print("What's your guess between 1 and 99?")
	guess = input()
	if guess == "exit":
		return ("exit")
	elif not guess.isnumeric():
		print("That's not a number.")
		return("continue")
	elif int(guess) == n:
		return ("success") 
	elif int(guess) > n:
		print("Too high!")
	elif int(guess) < n:
		print("Too low!")
	return("continue")

random.seed()
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
tries = 0
ret = ""
n = random.randint(1, 99)
while ret != "exit" and ret != "success":
	ret = guess(n)
	tries+=1
if ret == "exit":
	print("Goodbye!")
elif ret == "success":
	if n == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if tries == 1:
		print("Congratulations! You got it on your first try!")
	else:
		print("Congratulations, you've got it!")
		print("You won in",tries,"attempts!")

