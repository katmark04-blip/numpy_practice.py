import numpy as np

rng = np.random.default_rng()
array1=np.array([1,2,3,4,5,6])

print(rng.integers(low=1,high=10))

print(rng.integers(low=1,high=10,size=(2,4)))

# how to shuffle an array

rng.shuffle(array1)
print(array1)
#to make raandom choices from the arrray
num=rng.choice(array1)
print(num)