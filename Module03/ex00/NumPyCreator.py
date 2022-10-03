import numpy as np
import warnings
warnings.filterwarnings("error")
from random import random

class NumPyCreator:
    def from_list(self, lst, dtype=None):
        if isinstance(lst, list):
            try:
                return (np.array(lst, dtype=dtype))
            except:
                return None
    
    def from_tuple(self, tpl, dtype=None):
        if isinstance(tpl, tuple):
            try:
                return (np.array(tpl, dtype=dtype))
            except:
                return None
    
    def from_iterable(self, itr, dtype=None):
        try:
            iter(itr)
            return(np.array(list(itr), dtype=dtype))
        except:
            return None
    
    def from_shape(self, shape, value = 0, dtype=None):
        try:
            return (np.full(shape, value, dtype=dtype))
        except:
            return None

    def random(self, shape, dtype=None):
        try:
            arr = np.zeros(shape, dtype=dtype)
            for i in range(shape[0]):
                    for j in range(shape[1]):
                        arr[i][j] = random()
            return arr
        except:
            return None
    
    def identity(self, n):
        if isinstance(n, int) and n >=0 :
            return np.identity(n)