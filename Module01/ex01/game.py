class GotCharacter:
    def __init__(self, first_name=None, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive
    

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

class Lannister(GotCharacter):
    """A class representing the Lannister Family. A Lannister always pays its debts"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear me roar"

# from game import Stark, Lannister

# arya = Stark("Arya")
# print(arya.__dict__)
# arya.print_house_words()
# print(arya.is_alive)
# arya.die()
# print(arya.is_alive)

# tyrion = Lannister("Tyrion")
# print(tyrion.__dict__)
# tyrion.print_house_words()
# tyrion.die()
# print(tyrion.is_alive)