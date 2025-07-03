import numpy as np

# arr = np.array(16)
# arr = np.array([1,2,3,4, 5.5], dtype=np.int8)

arr = np.array([[[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]])

print(arr.dtype)
print(arr.ndim)
print(arr[1,0,2])
