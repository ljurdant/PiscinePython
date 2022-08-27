import sys

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 2:
	number = sys.argv[1]
	if number.isnumeric():
		n = int(number)
		print("I'm",end=' ')
		if n == 0:
			print("Zero.")
		elif n % 2 == 0:
			print("Even.")
		else:
			print("Odd.")
	else:
		print("AssertionError: argument is not an integer")
