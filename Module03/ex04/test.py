from csvreader import CsvReader
from Kmeans import KmeansClustering
import numpy as np

with CsvReader("solar_system_census.csv", skip_top=1) as file:
    x = np.array(file.getdata())[:,1:]
    km = KmeansClustering()
    km.fit(x)