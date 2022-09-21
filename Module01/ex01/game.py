class GotCharacter:
    """A class representing any GOT character. How long will they survive?"""
    def __init__(self, first_name=None, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    """A class representing the Lannister Family. A Lannister always pays its debts"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear me roar"

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

# from game import Stark, Lannister, GotCharacter

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)

tyrion = Lannister("Tyrion")
print(tyrion.__dict__)
tyrion.print_house_words()
tyrion.die()
print(tyrion.is_alive)

default = GotCharacter()
print(default.__dict__)

luigi = GotCharacter("Name", True)
print(luigi.__dict__)
print(luigi.__doc__)