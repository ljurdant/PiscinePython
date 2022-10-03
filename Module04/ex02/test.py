from ProportionBySport import proportion_by_sport
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../athlete_events.csv")
fl.display(df, 5)
pbs = proportion_by_sport(df, 2004, "Tennis", "F")
print(pbs)