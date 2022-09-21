import time
from random import randint
import os
#... your definition of log decorator...

def log(func):
    def timeformatter(t):
        if t < 1:
            return (str(round(t*1000, 3))+"ms")
        elif t < 60:
            return (str(round(t, 3))+"s")
        else:
            return (str(round(t / 60, 3)+"min"))

    def wrapper(*args):
        f = open('machine.log', 'a')
        msg = "("+os.environ["USER"]+")Running: "
        funcname = ' '.join(s[0].upper()+s[1:] for s in func.__name__.split("_"))
        if len(funcname) < 20:
            funcname = funcname.ljust(20, " ")
        else:
            funcname = funcname[:20]
        msg+=funcname
        start = time.time()
        r = func(*args)
        end = time.time()
        msg+="[ exec-time = "+timeformatter(end-start)+" ]"
        print(msg,file=f)
        f.close()
        return r
    return wrapper

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)