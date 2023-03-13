import numpy as np

numbers = np.array([0,5,10,15,25,50,75])

result1=numbers[5]     # 5. index
result2=numbers[-1]    # last index
result3=numbers[0:3]   # 0. 1. 2. index
result4=numbers[:3]    # 0. 1. 2. index 
result5=numbers[3:]    # 3. trough last index
result6=numbers[::]    # all of the ixdexs
result7=numbers[::-1]  # gives the reverse
result8=numbers[::-2]  # gives the reverse and two skips two

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)

# multi array
numbers2 = np.array([[0,5,10],[15,25,50],[75,80,85]])

result9 = numbers2[0]     # 0. index [0,5,10]
result10 = numbers2[2]    # 2. index [75,80,85]
result11 = numbers2[0,2]  # the 0. line 2. column index
result12 = numbers2[2,2]  # the 2. line 2. column index
result13 = numbers2[:,2]  # all 2. column
result14 = numbers2[:,0]  # all 0. column
result15 = numbers2[:,0:2]  # all 0. column and to 2. index (2. not included)
result16 = numbers2[-1,:]  # the last index and all of them
result17 = numbers2[:2,:2] # gives [00 01] [10 11] 

print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
print(result15)
print(result16)
print(result17)

# reference coping meaning adrees coping
array1 = np.arange(1,10)
array2 = array1  

print(array1)
print(array2)

# changing in array2 changes in array1
array2[0] = 20
print(array1)
print(array2)

# copy() function
array3 = np.arange(1,11)
array4 = array3.copy()

print(array3)
print(array4)

# changing in array4 does not change in array3
array4[0] = 20
print(array3)
print(array4)








