import pandas as pd

df = pd.read_csv("D:\mark\python\__pycache__\data.csv.txt")

#### Data cleaning ###

### REmoving columns ###
#df= df.drop(columns=["Name","Type2"])

#### Removing rows with missing data and filliing in new data###
#df= df.dropna(subset=["Type2"])
#df= df.fillna({"Type2":"no value"})

#### replacing values in column with other values ####
#df =df.replace({"Grass":"GRASS","Poison":"POISON"})
### to replace a specific value in a specific column ###
#df["Type2"] =df["Type2"].replace({"Grass":"GRASS","Poison":"POISON"})

### standardising values in a column e.g making all column values capital ###
#df["Name"] =df["Name"].str.upper()
df["Name"] =df["Name"].str.lower()

print (df.to_string())
