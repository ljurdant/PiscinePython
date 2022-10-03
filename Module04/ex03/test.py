from HowManyMedals import how_many_medals
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../data/athlete_events.csv")
# fl.display(df, 5)
print(how_many_medals(df, 'Kjetil Andr Aamodt'))