import pandas as pd


com= {"Name":["Mark","Aaron","Katenda"],"Height":[123,124,231]}


#how to create a data frame

df= pd.DataFrame(com,index=["n1","n2","n3"])


#how to create a new column
df["Age"]=[21,22,19]

#how to create new rows
newrow= pd.DataFrame([{"Name":"donmish","Height": 222,"Age":24},
                      {"Name":"badass","Height": 211,"Age":28}],
                      index=["n4","n5"])

df= pd.concat([df,newrow])


print(df)