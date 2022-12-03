# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:43:09 2022

@author: marin
"""

import numpy as np

"""
Create arrays
"""

data = np.random.rand(2,3,4) # random values
zeroes = np.zeros((2,2,2)) # Zero values
full = np.full((2,2,2),7)   # Values that are set - 7
ones = np.ones((2,2,2)) # Value of 1

arr = np.array([[1,2,3,4],[2,3,4,5],[6,7,8,9]])

"""
Readin arrays
"""

shape = data.shape
size = data.size
types = data.dtype

#slicing
arr = data[0]
slicer = data[0][0:2]
reverse = data[-1]
singlevalue = data[0][0][0]


#Update
list1 = np.random.rand(10)
list2 = np.random.rand(10)

add = np.add(list1,list2)
Sub = np.subtract(list1,list2)
div = np.divide(list1,list2)
mul = np.multiply(list1,list2)
dot = np.dot(list1,list2)

sqrt = np.sqrt(25)
sortedList = list1.sort()


"""
Chaange shape
"""

ShapeData = data.reshape((2,2,-1))
ShapeData.shape

# append to arra
zeroes = np.append(zeroes,[3,4])
# insert
zeroes = np.insert(zeroes,2,1)
print (zeroes)

# delete
zeroes = np.delete(zeroes,2)
print(zeroes)

# save array
np.save("ArraySample", data)

SavedArray = np.load("ArraySample.npy")





