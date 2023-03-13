import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))  #<class 'list'>
print(type(np_array)) #<class 'numpy.ndarray'>

# python multi list
py_multi = [1,2,3],[4,5,6],[7,8,9]

# numpy multi aray reshaping
np_multi = np_array.reshape(3,3)

print(py_multi)
print(np_multi)

#boyutuna bakmak için
print(np_array.ndim)
print(np_multi.ndim)

#looking shape
print(np_array.shape)
print(np_multi.shape)