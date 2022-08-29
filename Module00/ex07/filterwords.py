import sys
import string


def filterwords(S: str, n: int):
	words = S.split()
	filtered = []
	for word in words:
		if sum(c not in string.punctuation for c in word) > n:
			for p in string.punctuation:
				word = word.replace(p, '')
			filtered.append(word)
	return (filtered)

if len(sys.argv) != 3:
	print("ERROR")
else:
	S = sys.argv[1]
	n = sys.argv[2]
	if not n.isnumeric():
		print("ERROR")
	else:
		print(filterwords(S, int(n)))