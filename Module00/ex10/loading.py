from time import sleep
from time import time
import math
import sys
import curses
def proper_round(n: float):
    if (n - round(n)) >= 0.5:
        n = math.ceil(n)
    else:
        n = round(n)
    return (n)

def ft_progress(lst):
    loading_constant = 25
    start = time()
    second = 0
    previous_message = ""
    for i in range(len(lst)):
        if i == 1:
            second = time()
        current = time()
        percent = proper_round((i/len(lst) * 100))
        loading = proper_round(loading_constant * percent / 100)
        elapsed_time = current - start
        elapsed_time = "{:.2f}".format(elapsed_time)
        if i >= 1:
            ETA = (second - start) * (len(lst) - i)
            ETA = "{:.2f}".format(ETA)
        else:
            ETA = 0
        message = "ETA "+str(ETA)+"s ["+(3-len(str(percent)))*" "+str(percent)+"%]["+loading*"="+">"+(loading_constant - loading)*" "+"]"+str(i)+"/"+str(len(lst))+" | elapsed time "+str(elapsed_time)+"s"
        if len(previous_message) > len(message):
            message+=(len(previous_message) - len(message)) * " "
        previous_message = message
        print(message)
        yield lst[i]

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(1)
print()
print(ret)