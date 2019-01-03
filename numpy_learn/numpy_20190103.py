import numpy as np

# learn ndarray
# create a ndarray
data1 = [6, 7.5, 8, 0, 1]  # a normal list
test_arr = np.array(data1)
print(test_arr)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
test_arr_2 = np.array(data2)
print(test_arr_2)
print(test_arr_2.ndim)
print(test_arr_2.shape)
print(test_arr_2.dtype)
# some contributes of a ndarray

print(np.zeros(10))
print(np.zeros((3, 6)))

# np.empty not return all zero but some rubbish values
print(np.empty((2, 3, 2)))

# numpy's array
print(np.array(15))

test_tuple = (1, 2, 3, 4, 5)
tuple_array = np.array(test_tuple)
print(tuple_array)

test_arr_3 = np.asarray(test_arr_2)
print(test_arr_3)

print(np.ones_like(test_arr_3))

# create an identity matrix
print(np.identity(6, dtype=int))

# ndarray contains many kinds of datatype including complex number
test_type = np.array([1, 2, 3, 4, 5])
print(test_type.dtype)
# tranform datatype
float_type = test_type.astype(np.float64)
print(float_type.dtype)

# vector multiplication
test_mul = np.array([1, 2, 3, 4])
print(test_mul * test_mul)

test_mul = np.array([[1, 2, 3, 4], [1, 3, 5, 7]])
print(test_mul * test_mul)

# broadcasting
print(1/test_mul)
print(test_mul**0.5)

# slice of a ndarray
test_slice = np.arange(10, 100, 2)
print(test_slice)
print(test_slice[1:20])

test_slice[1:5] = 9999
print(test_slice)  # also for broadcasting

# numpy array is special , it seldom copy itself even in slicing
a_slice = test_slice[1:5]
a_slice[:] = [1, 2, 3, 4]
print(test_slice)

# multi-level array
ml_arr = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(ml_arr[2])
print(ml_arr[1, 2])

arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6]],
                   [[7, 8, 9],
                   [10, 11, 12]]])
print(arr_3d)
print(arr_3d[1])
print(arr_3d[0, 1])
print(arr_3d[0, 1, 1])

# 进行索引时务必记住，所有用“:”写出的所有区间都是左闭右开的。
print(arr_3d[0, 0, :2])

