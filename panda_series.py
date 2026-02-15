import pandas as pd

scores={"math": 92,"phy": 88,"econ": 70,"bio":67}
array=[2,5,8,1,9]

serie= pd.Series(array,index=("house 1","house 2","house 3","house 4","house 5"))

marks=pd.Series(scores)

print(serie)
print(serie.iloc[2])
print(serie.loc["house 4"])


print(marks)
print(marks.loc["phy"])
print(marks[(marks>74)])
print(marks[(marks>74) & (marks<90)])