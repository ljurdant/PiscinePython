class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        length = len(x)
        if length:
            return(sum(x) / length)

    def median(self, x):
        length = len(x)
        mid = length // 2
        ordered = sorted(x)
        if length % 2:
            return ordered[mid] / 1
        elif length:
            return (ordered[mid] + ordered[mid - 1]) / 2
    
    def quartile(self, x):
        length = len(x)
        ordered = sorted(x)
        if length:
            quotient = (length - 1) / 4
            first = ordered[int(quotient)] + (quotient - int(quotient)) * (ordered[int(quotient) + 1] - ordered[int(quotient)])
            quotient*=3    
            third = ordered[int(quotient)] + (quotient - int(quotient)) * (ordered[int(quotient) + 1] - ordered[int(quotient)])
            return ([first, third])
            
    def var(self, x):
        length = len(x)
        if length:
            mean = self.mean(x)
            return (sum((i - mean)**2 for i in x) / length)
    
    def std(self, x):
        if len(x):
            return (self.var(x)**0.5)