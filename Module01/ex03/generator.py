import random
import numpy as np

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.'''
    if option == None:
        option = "none"
    options = ["shuffle", "ordered", "unique", "none"]
    if type(text) != str or option not in options:
        return ("ERROR")
        
    text = text.split(sep)
    if option == "shuffle":
        random.seed()
        indices = random.sample(range(len(text)), len(text))
        for i in range(len(text)):
            yield text[indices[i]]
    elif option == "unique":
        arr = np.array(text)
        uniques = np.unique(arr)
        for word in uniques:
            yield word
    elif option == "ordered":
        for word in sorted(text):
            yield word
    else:
        for word in text:
            yield word