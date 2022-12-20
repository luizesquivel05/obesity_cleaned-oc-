import pandas as pd
import numpy as np

# TRATAMENTO INICIAL:
def obesityT():
    obesity = pd.read_csv("Data/obesity_cleaned.csv")
    del obesity["Unnamed: 0"]
    obesity["Obesity"] = obesity["Obesity (%)"].apply(lambda x: x.split(" ")[0])
    obesity.loc[obesity["Obesity"] == "No", "Obesity"] = np.nan
    obesity.dropna(inplace=True)
    obesity["Obesity"] = obesity["Obesity"].astype(float)
    obesity.set_index("Year", inplace=True)
    return obesity
data = obesityT()

# QUESTION 0:
def obesityforsex():
    print(data[data.index == 2015].groupby("Sex").mean())

# QUESTION 1:
def maxandmintaxobesity():
    obesity_start = data[data.index == 1975]
    obesity_end = data[data.index == 2016]
    obesity_start.set_index("Country", inplace=True)
    obesity_end.set_index("Country", inplace=True)
    obesity_ev = obesity_end[obesity_end["Sex"] == "Both sexes"]["Obesity"] - obesity_start[obesity_start["Sex"] == "Both sexes"]["Obesity"]
    print(obesity_ev.sort_values().dropna().head(5))
    print(obesity_ev.sort_values().dropna().tail(5))

# QUESTION 2:
def maxmintaxobesityin2015():
    mmy2015 = data[data.index == 2015].copy()
    print(mmy2015[mmy2015["Obesity"] == mmy2015["Obesity"].max()])
    mmy2015 = data[data.index == 2015].copy()
    print(mmy2015[mmy2015["Obesity"] == mmy2015["Obesity"].min()])

# QUESTION 3:
def worldandbrazil():
    df_brasil = data[data["Country"] == "Brazil"]
    print((df_brasil[df_brasil["Sex"] == "Female"]["Obesity"] - df_brasil[df_brasil["Sex"] == "Male"]["Obesity"]))
