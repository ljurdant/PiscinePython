import pandas as pd

def youngest_fellah(df, year):
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int):
        print("Error: argument type")
    else:
        data = {
            "F":"",
            "M":""
        }
        for key in data.keys():
            data[key] = df.query("Year==@year and Sex==@key")["Age"].min()
        return (data)