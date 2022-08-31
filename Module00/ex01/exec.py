import sys

args = sys.argv
for i in range(len(sys.argv) - 1, 0, -1):
	words = args[i].split()
	words.reverse()
	lsts = []
	for word in words:
		lst = []
		for letter in word:
			if letter.isupper():
				letter = letter.lower()
			elif letter.islower():
				letter = letter.upper()
			lst.append(letter)
		lst.reverse()
		word = ''.join(lst)
		lsts.append(word)
	print(' '.join(lsts), end=(' ', '\n')[i == 1])