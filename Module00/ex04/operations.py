import sys

def isnumber(number):
	if len(number) == 0:
		return False
	elif (number[0] == '-' and number[1:].isnumeric()) or number.isnumeric():
		return True
	else:
		return False


if len(sys.argv) > 3:
	print("AssertionError: too many arguments")
elif len(sys.argv) != 3:
	print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
	A = sys.argv[1]
	B = sys.argv[2]
	print(isnumber(B))
	if not isnumber(A) or not isnumber(B):
		print("AssertionError: only integers")
	else:
		A = int(A)
		B = int(B)
		print("Sum:\t", A+B, sep="\t")
		print("Difference:", A-B, sep="\t")
		print("Product:", A*B, sep="\t")
		if B != 0:
			print("Quotient:", A/B, sep="\t")
			print("Modulo:\t", A%B, sep="\t")
		else:
			print("Quotient:", "ERROR (division by zero)", sep="\t")
			print("Modulo:\t","ERROR (modulo by zero)", sep="\t")
