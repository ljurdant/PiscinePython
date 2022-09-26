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