import pandas as pd


####how to import an csv file
# By adding>>,index_col=["Name"]<< the indexing of the file 
# changes from numbers to names of the characters######
df= pd.read_csv("D:\mark\python\__pycache__\data.csv.txt",index_col=["Name"])

###how to print the whole file###
#print(df)

####how to print specific columns of the file###
#print(df["Type1"].to_string())

###how to print multiple columns of the file####
#print(df[["Type1","Name","Height"]])

####how to print rows####
#print(df)
#print(df.iloc[3])
#print(df.loc["Mewtwo"])

###To print specific stuff just create a list of the stuffyou want to print###
#print(df.loc["Moltres",["Type2","Height"]])

### A simple program###
pokeman_name= input("Enter the name of the pkeman to know its details : ")

try:
 print(df.loc[pokeman_name,["Type2"]])
except KeyError:
 print(f"{pokeman_name} that name does not exist") 
