class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) == len(words):
            return sum(coef*len(word) for coef, word in zip(coefs, words))
        else:
            return -1
    def enumerate_evaluate(coefs, words):
        if len(coefs) == len(words):
            return sum(coefs[index]*len(word) for index, word in enumerate(words))
        else:
            return -1