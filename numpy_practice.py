import numpy as np


array = np.array([[2,4,5,8],
                  [2,5,8,0],
                  [4,7,1,3], 
                  [7,7,7,7]])

#for x in array:
#    print(x)
#print(array.shape)
#print(array[1:3])
#print(array.ndim)
#print(array[1,0,1] ,array[0,0,0] ,array[2,0,0])
print(array[::1])#this is for raws

print(array[:, 0:5:2])#this is for columns
print(array[:, ::-1])
print(array[1:3, 0:3])#this is both for rows and columns