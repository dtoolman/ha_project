import pandas as pd

data = pd.read_csv("export.csv")

data["Item: Small Bag"] = ""
data["Item: Medium Bag"] = ""
data["Item: Large Bag"] = ""

for i, entry in enumerate(data["Task Details (Bag Color)"]):
    l = entry.lower();

    if "white" in l:
        col = "Item: Small Bag"
    elif "green" in l:
        col = "Item: Medium Bag"
    elif "blue" in l:
        col = "Item: Large Bag"
    else:
        raise ValueError("Unable to determine bag size from entry '" + entry + "' at row " + str(i) + ". Try 'white', 'green', or 'blue'.")
    
    data.loc[i, col] = data["Quantity"][i];

data.to_csv(path_or_buf="finished.csv")
