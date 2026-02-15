import pandas as pd

df= pd.read_csv("D:\mark\python\__pycache__\data.csv.txt")


###    filtering in pandas     ####
#tall_guys = df[df["Height"] >= 2.5]
#fat_guys = df[df["Weight"] >= 230]
#giant_guys = df[(df["Height"] >= 2.0) & (df["Weight"] >= 230)]

#print(giant_guys)

####    Aggretion in pandas #######
# we add >>>numeric_only= True<<<< because not 
# all columns have numeric values
#print(df.mean(numeric_only= True))
#print(df.max(numeric_only= True))
#print(df.min(numeric_only= True))
#print(df.count())

### for specific columns###
#print(df["Weight"].mean())
#print(df["Weight"].max())
#print(df["Weight"].min())

##### grouping by####

grouppie = df.groupby("Type2")

print(grouppie["Weight"].max())
print(grouppie["Weight"].min())
print(grouppie["Weight"].mean())