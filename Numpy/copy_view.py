import numpy as np
from pprint import pprint

arr = np.full((4,4), 10)

arr2 = arr.view()

arr[1,1] = 99
arr[2,2] = 88
arr2[3,3] = 77

pprint(arr)
print(id(arr))
pprint(arr2)
print(id(arr2))
print(arr2.base)