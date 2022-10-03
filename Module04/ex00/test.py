import pandas as pd
from FileLoader import FileLoader

fl = FileLoader()
data = fl.load("../data/athlete_events.csv")
# fl.load(None)
fl.display(data, -3)
# fl.display(None, None)