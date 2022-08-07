import pandas as pd
import math

data = pd.read_csv("export.csv")

data["Task Details (Bag Color)"] = ""

for i in range(len(data.index)):

    if not math.isnan(data.loc[i, "Item: Small Bag"]):
        color = "White"
    elif not math.isnan(data.loc[i, "Item: Medium Bag"]):
        color = "Green"
    elif not math.isnan(data.loc[i, "Item: Large Bag"]):
        color = "Blue"
    else:
        raise ValueError("Bag quantities at row " + i + " are invalid")
    
    data.loc[i, "Task Details (Bag Color)"] = color;

data.to_csv(path_or_buf="finished.csv")
