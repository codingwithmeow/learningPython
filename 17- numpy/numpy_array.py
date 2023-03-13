import numpy as np

array = np.array([1,3,5,7,9])
print(array)

array2 = np.arange(1,10)   # array2 = [1 2 3 4 5 6 7 8 9] 
print(array2)

array3 = np.arange(10,100,3)  # between 10 and 100 increaing 3
print(array3)

array4 = np.zeros(10) # with shape = 10 made of zero float
print(array4)

array5 = np.ones(10) # with shape = 10 made of one float
print(array5)

array6 = np.linspace(0,100,5) #between 0 and 100 with equal 5 parts float
print(array6)

array7 = np.linspace(0,5,5) #between 0 and 5 with equal 5 parts float
print(array7)

# making random variables
array8 = np.random.randint(1,10) # creates a random int number between 1 and 10 (10 not including)
print(array8)

array9 = np.random.randint(20) # creates a random int number between 0 and 20 (20 not including)
print(array9)

array10 = np.random.randint(1,10,3) # creates 3 matriw with a random int number between 1 and 10 (10 not including)
print(array10)

array11 = np.random.rand(5) # creates 5 random float number between 0 and 1 
print(array11)

array12 = np.random.randn(5) # creates 5 random float number between -infinite and infinite 
print(array12)

#reshaping matrixes
array13 = np.arange(50)
array14 = array13.reshape(5,10) #making array to 5 to 10 matrix
print(array13)
print(array14)

# sum of rows
sum_row = array14.sum(axis=1)
print(sum_row)

# column of rows
sum_column = array14.sum(axis=0)
print(sum_column)

#finding max, min, mean, value
array15 = np.random.randint(1,100,10)
max = array15.max()
min = array15.min()
mean = array15.mean()
max_index = array15.argmax() # max numbers index
min_index = array15.argmin() # min numbers index
print(array15)
print(max)
print(min)
print(mean)
print(max_index)
print(min_index)
