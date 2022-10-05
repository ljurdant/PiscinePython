from MyPlotLib import MyPlotLib
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../data/athlete_events.csv")
mpl = MyPlotLib()
# mpl.histogram(df, ["Age","Height","Name","Medal","Year"])
# mpl.density(df, ["Weight","Height","Name"])
# mpl.pair_plot(df, ["Weight", "Height"])
# mpl.box_plot(df, ["Weight", "Height"])
