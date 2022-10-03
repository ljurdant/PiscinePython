import pandas as pd

def how_many_medals(df, name):
    if not isinstance(df, pd.DataFrame) or not isinstance(name, str):
        print("Error: Bad argument types")
    else:
        dfname =  df.query("Name==@name")
        if not len(dfname):
            print(name,"never participated in th eolympics")
        else:
            medal_details = {"G":"Gold","S":"Silver","B":"Bronze"}
            medal_keys = {"G":0, "S":0, "B":0}
            years = dfname["Year"].unique()
            medal_total = dict()
            for year in years:
                medals = {"G":0, "S":0, "B":0}
                for key in medal_keys.keys():
                    mk = medal_details[key]
                    medals[key] = len(dfname.query("Medal== @mk and Year==@year"))
                medal_total[year] = medals
            return (medal_total)