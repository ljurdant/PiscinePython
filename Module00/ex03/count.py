import string
import sys

def analyze(text):
	upper = sum([c.isupper() for c in text])
	lower = sum([c.islower() for c in text])
	punctuation = sum([c in string.punctuation for c in text])
	space = sum([c == ' ' for c in text])
	print("The text contains",len(text),"characters:")
	print("-",upper," upper letter(s)")
	print("-",lower," lower letter(s)")
	print("-",punctuation,"punctuation mark(s)")
	print("-",space,"space(s)")

def text_analyzer(text = None):
	"""
This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
	if text == None:
		print("What is the text to analyze?")
		analyze(input())
	elif type(text) != str:
		print("AssertionError: argument is not a string")
	else:
		analyze(text)

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 2:
	text_analyzer(sys.argv[1])