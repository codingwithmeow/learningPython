import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(f"numbers1 = {numbers1}")
print(f"numbers2 = {numbers2}")

# addition 
result1 = numbers1 + numbers2   # adding two arrays
result2 = numbers1 + 10         # adds all index 10

print(f"numbers1 + numbers2 = {result1}")
print(f"numbers1 + 10 = {result2}")

# subtraction
result3 = numbers1 - numbers2   # subtracts two arrays
result4 = numbers1 - 10         # subtracts all index 10

print(f"numbers1 - numbers2 = {result3}")
print(f"numbers1 - 10 = {result4}")

# multiplication
result5 = numbers1 * numbers2   # multiplicats two arrays
result6 = numbers1 * 10         # multiplicats all index 10

print(f"numbers1 * numbers2 = {result5}")
print(f"numbers1 * 10 = {result6}")

# division
result7 = numbers1 / numbers2   # divides two arrays
result8 = numbers1 / 10         # divides all index 10

print(f"numbers1 / numbers2 = {result7}")
print(f"numbers1 / 10 = {result8}")

# another equations
result9 = np.sin(numbers1)    
result10 = np.cos(numbers1) 
result11 = np.sqrt(numbers1)
result12 = np.log(numbers1)

print(f"sin(numbers1) = {result9}")
print(f"cos(numbers1) = {result10}")
print(f"square root of numbers1 = {result11}")
print(f"log of numbers1 = {result12}")

# making multi array
numbers3 = numbers1.reshape(2,3)
numbers4 = numbers2.reshape(2,3)

print(f"reshape by numbers1 with (2,3) is numbers3 = {numbers3}")
print(f"reshape by numbers2 with (2,3) is numbers4 = {numbers4}")

# combining arrays 
numbers5 = np.vstack((numbers3,numbers4))
numbers6 = np.hstack((numbers3,numbers4))

print(f"combining numbers3 and numbers4 with vstack() (vertical combining) numbers5 = {numbers5}")
print(f"combining numbers3 and numbers4 with hstack() (horizontal combining) numbers5 = {numbers6}")

# booling operations
result13 = numbers1 >= 50
result14 = numbers1 %2 == 0

print(f"is numbers1 indexs bigger or equal to 50 : {result13}")
print(f"is numbers1 indexs even number : {result14}")
