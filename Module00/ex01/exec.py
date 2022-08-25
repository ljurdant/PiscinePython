import sys

args = sys.argv
for i in range(len(sys.argv) - 1, 0, -1):
	words = args[i].split()
	words.reverse()
	for word in words:
		for j in range(len(word) - 1, -1, -1):
			if word[j].islower():
				print(word[j].upper(), end='')
			else:
				print(word[j].lower(), end='')
		print(' ', end='')