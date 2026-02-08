import numpy as np


array1 = np.array([[21,43,62,95],
                  [12,14,16,19]])

teens= array1[(array1>18) & (array1<30)]
oldies= array1[array1>40]
evens=array1[array1%2==0]
odds=array1[array1%2!=0]

print(odds)
print(oldies)
print(teens)
print(evens)