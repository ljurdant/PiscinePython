from YoungestFellah import youngest_fellah
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../athlete_events.csv")
yf = youngest_fellah(df, 2010)
print(yf)