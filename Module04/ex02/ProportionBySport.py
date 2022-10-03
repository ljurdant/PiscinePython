import pandas as pd

def proportion_by_sport(df, year, sport, gender):
    dfq = df.query("Year==@year and Sex==@gender")
    dfq = dfq.drop_duplicates(subset = ["ID"])
    return (len(dfq.query("Sport==@sport"))/len(dfq))

