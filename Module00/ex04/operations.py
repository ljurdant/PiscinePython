import sys

if len(sys.argv) > 3:
	print("AssertionError: too many arguments")
elif len(sys.argv) != 3:
	print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
	A = sys.argv[1]
	B = sys.argv[2]
	if not A.isnumeric() or not B.isnumeric():
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
