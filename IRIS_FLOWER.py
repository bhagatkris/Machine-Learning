import pandas as pd
from pandas.plotting import scatter_matrix


#read_csv is a panda fx to read a csv file type
df = pd.read_csv("avocado.csv")

regions = df["region"].unique()

df = df.copy()[df["type"] ==  "organic"]

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by = "Date", ascending = True, inplace = True)

graph_df = pd.DataFrame()

for region in regions:
    #print(region)
    region_df = df.copy()[df["region"] == region]
    region_df.set_index("Date", inplace = True)
    region_df.sort_index(inplace = True)
    region_df.dropna()
    region_df[f"{region}_Price25MA"] = region_df["AveragePrice"].rolling(25).mean()
    
    if graph_df.empty:
        graph_df = region_df[[f"{region}_Price25MA"]]
        #print(graph_df.tail())
        
    else:
        graph_df = graph_df.join([region_df[f"{region}_Price25MA"]])
        
graph_df.tail(3)

graph_df.dropna().plot(figsize = (8, 5), legend = False)