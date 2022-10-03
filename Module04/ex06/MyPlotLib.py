import pandas as pd
import numpy as np

class MyPlotLib:
     def histogram(self, data, features):
        for f in features:
            hist = data[f].hist()
            