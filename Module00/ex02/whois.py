import sys

def isnumber(number):
	if len(number) == 0:
		return False
	elif (number[0] == '-' and number[1:].isnumeric()) or number.isnumeric():
		return True
	else:
		return False

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 2:
	number = sys.argv[1]
	if isnumber(number):
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
