import sys

morse = {
	"A": " ._", "B": "-...", "C": "-.-.", "D": "-..","E" :".","F": "..-.","G":"--.", "H":"....","I" :"..","J" :".---", "K" :"-.-",
	"L":".-..", "M":"--", "N":"-.", "O" :"---", "P" :".--.", "Q" :"--.-","R":".-.","S":"...","T" :"-","U" :"..-","V" :"...-",
	"W" :".--","X" :"-..-","Y" :"-.--","Z" :"--..","0" :"-----","1" :".----","2" :"..---","3" :"...--","4" :"....-","5" :".....",
	"6" :"-....","7" :"--...","8" :"---..","9" :"----.", " ": "/"
}

if len(sys.argv) > 1:
	sys.argv.pop(0)
	message = " ".join(sys.argv).upper()
	code = ""
	b = 1
	for c in message:
		if c not in morse:
			b = 0
		else:
			code+=morse[c]+" "
	if b:
		print(code[:len(code) - 1])
	else:
		print("ERROR")