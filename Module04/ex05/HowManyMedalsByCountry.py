import pandas as pd
def how_many_medals_by_country(df, country):
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    medal_details = {"G":"Gold","S":"Silver","B":"Bronze"}
    dfcountry = df.query("Team==@country and not Medal.isnull()")
    years = sorted(dfcountry["Year"].unique())
    country_dict = dict()
    for year in years:
        dfyear = dfcountry.query("Year==@year")
        medals = {"G":0, "S":0, "B":0}
        for medal in medals.keys():
            key = medal_details[medal]
            medals[medal] =  len(dfyear.query("Sport in @team_sports").query("Medal==@key").drop_duplicates(subset = ["Event"])) + len(dfyear.query("Sport not in @team_sports").query("Medal==@key"))
            
        country_dict[year] = medals
    return (country_dict)
