import numpy as np

# make numpy array with (10,15,30,45,60) 
array1 = np.array([10,15,30,45,60])
print(f"numpy array with (10,15,30,45,60) = {array1}")

# make numpy array with between 5 and 15
array2 = np.arange(5,16)
print(f"numpy array with between 5 and 15 = {array2}")

# Create a numpy array by increasing 5 by 5 between (50-100)
array3 = np.arange(50,100,5)
print(f" numpy array by increasing 5 by 5 between (50-100) = {array3}")

# make numpy array with zeros and 10 elements
array4 = np.zeros(10)
print(f"numpy array with zeros and 10 elements = {array4}")

# make numpy array with one and 10 elements
array5 = np.ones(10)
print(f"numpy array with one and 10 elements = {array5}")

# 6- Generate 5 evenly spaced numbers (0-100).
array6 = np.linspace(0,100,5)
print(f"5 evenly spaced numbers (0-100) = {array6}")

# 7- Generate 5 random integers between (10-30).
array7 = np.random.randint(10,30,5)
print(f"5 random integers between (10-30) = {array7}")

# 8- Generate 10 numbers from [-1 to 1].
array8 = np.random.randn(10)
print(f" 10 numbers from [-1 to 1] = {array8}")

# 9- Generate a random matrix of (3x5) dimensions between (10-50).
array9 = np.random.randint(10,50,3*5).reshape(3,5)
print(f"random matrix of (3x5) dimensions between (10-50) matrix = {array9}")

# 10- Calculate the sum of the row and column numbers of the produced matrix in 9 ?
rowTotal = array9.sum(axis=1)
columnTotal = array9.sum(axis=0)
print(f"matrixes row total = {rowTotal} and column total = {columnTotal}")

# 11- What is the largest, smallest and average of the produced matrix in 9?
max = array9.max()
min = array9.min()
mean = array9.mean()
print(f"matrixes max value = {max} , min value = {min} and mean value = {mean}")

# 12- What is the index of the largest value and the smallest value of the produced matrix in 9?
argmax = array9.argmax()
argmin = array9.argmin()
print(f"matrixes max value index = {argmax} , min value index = {argmin} ")

# 13- Select the first 3 elements of the array containing numbers (10-20).
array10 = np.arange(10,20)
select = array10[:3]
print(f"array = {array10} and first 3 index = {select}")

# 14- Print the elements of the generated array in 13 in reverse.
result1 = array10[::-1]
print(f"array = {array10} and reverse = {result1}")

# 15- Select the first row of the generated matrix in 9.
result2 = array9[0]
print(f" the first row of the matrix = {result2}")


# 16- Which is the element in the 2nd row and 3rd column of the produced matrix in 9?
result3 = array9[2,3]
print(f" 2nd row and 3rd column of the matrix = {result3}")


# 17- Select the first element in all rows of the generated matrix in 9.
result4 = array9[:,0]
print(f"first element in all rows of the matrix = {result4}")

# 18- Take the square of each element of the generated matrix in 9.
result5 = array9 ** 2
print(f"square of each element of the matrix = {result5}")


# 19- Which of the produced matrix elements is a positive even number?
array11 = np.random.randint(-50,50,3*5).reshape(3,5)
even_numbers = array9[array11 %2 == 0]
even_numbers = even_numbers[even_numbers > 0]
print(f" numpy array with between -50 and 50 = {array11}")
print(f"positive even number of the matrix = {even_numbers}")
