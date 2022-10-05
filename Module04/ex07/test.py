from Komparator import Komparator
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../data/athlete_events.csv")
komp = Komparator(df)

# komp.compare_box_plots("Sex","Height") 
komp.density("Sex", "Weight")
# komp.compare_histograms("Sex","Height")