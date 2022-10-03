import pandas as pd

class SpatioTemporalData:
    def __init__(self, df) :
        self.df = df
    
    @property
    def df(self):
        return self._df
    @df.setter
    def df(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("df attribute must be a dataframe")
        self._df = value

    def when(self, location):
        if isinstance(location, str):
            return list(self.df.query("City==@location")["Year"].unique())
    
    def where(self, year):
        if isinstance(year, int):
            return list(self.df.query("Year==@year")["City"].unique())