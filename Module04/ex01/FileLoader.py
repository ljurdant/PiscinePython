from numpy import isin
import pandas as pd

class FileLoader:
    def load(self, path):
        if not isinstance(path, str):
            print("Error: path argument must be string")
        else:
            try:
                data = pd.read_csv(path)
            except FileNotFoundError as fnf:
                    print(fnf)
            else:
                return data
    def display(self, df, n):
        if not isinstance(n, int):
            print("Error: n argument must be an integer")
        elif not isinstance(df, pd.DataFrame):
            print("Error: df argument must be a Dataframe")
        else:
            if (n >= 0):
                print(df.head(n))
            else:
                print(df.tail(-n))
        