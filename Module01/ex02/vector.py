def shapeCheck(v1, v2):
    if v1.shape != v2.shape:
        raise ValueError("Vectors are not of the same shape")

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
    
    def dot(self, rhs):
        shapeCheck(self, rhs)
        result = 0
        if self.shape[0] == 1:
            result = sum([x * y for x,y in zip(self.values[0], rhs.values[0])])
        else:
            result = sum([x[0] * y[0] for x,y in zip(self.values, rhs.values)])
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
        return (transpose)
    
    def __add__(self, rhs):
        shapeCheck(self, rhs)
        if self.shape[0] == 1:
            
        return (result)