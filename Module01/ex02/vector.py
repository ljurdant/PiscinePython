import re


def shapeCheck(v1, v2):
    if v1.shape != v2.shape:
        raise ValueError("Vectors are not of the same shape")

def iterate_single(vector, function):
    lst = []
    if vector.shape[0] == 1:
        lst.append([])
        for x in vector.values[0]:
            lst[0].append(function(x))
    else:
        for x in vector.values:
            lst.append([function(x[0])])
    return (lst)

def iterate_double(vector, other, function):
    lst = []
    if vector.shape[0] == 1:
        lst.append([])
        for x, y in zip(vector.values[0], other.values[0]):
            lst[0].append(function(x, y))
    else:
        for x, y in zip(vector.values, other.values):
            lst.append([function(x[0], y[0])])
    return (lst)

class Vector:
    def __init__(self, values, end = None):
        if type(values) == int:
            start = 0
            if end == None:
                end = values
            else:
                start = values
            self.values = []
            for i in range(start, end):
                self.values.append([float(i)])
        else:
            self.values = values
        self.shape = (len(self.values), len(self.values[0]))
    
    def dot(self, other):
        shapeCheck(self, other)
        result = 0
        if self.shape[0] == 1:
            result = sum([x * y for x,y in zip(self.values[0], other.values[0])])
        else:
            result = sum([x[0] * y[0] for x,y in zip(self.values, other.values)])
        return result
    
    def T(self):
        transpose = []
        if self.shape[0] == 1:
            for x in self.values[0]:
                transpose.append([x])
        else:
            transpose.append([])
            for x in self.values:
                transpose[0].append(x[0])
        return (Vector(transpose))
    
    def __add__(self, other):
        shapeCheck(self, other)
        return (Vector(iterate_double(self, other, lambda x, y: (x + y))))

    def __radd__(self, other):
        shapeCheck(self, other)
        return (Vector(iterate_double(other, self, lambda x, y: (x + y))))

    def __sub__(self, other):
        shapeCheck(self, other)
        return (Vector(iterate_double(self, other, lambda x, y: (x - y))))


    def __rsub__(self, other):
        shapeCheck(self, other)
        return (Vector(iterate_double(other, self, lambda x, y: (x - y))))
    
    def __truediv__(self, scalar):
        if type(scalar) != float and type(scalar) != int:
            raise ValueError("Vector can only be divided by a scalar")
        if (scalar == 0):
            raise ZeroDivisionError("Can't divide by zero")
        return(Vector(iterate_single(self, lambda x: x / scalar)))
    
    def __rtruediv__(self, scalar):
        raise NotImplementedError("Division of scalar by a vector is not implemented")
    
    def __mul__(self, scalar):
        if type(scalar) != float and type(scalar) != int:
            raise ValueError("Vector can only be divided by a scalar")
        return (Vector(iterate_single(self, lambda x : x * scalar)))
    def __rmul__(self, scalar):
        if type(scalar) != float and type(scalar) != int:
            raise ValueError("Vector can only be divided by a scalar")
        return (Vector(iterate_single(self, lambda x : x * scalar)))
    