import numpy as np
from pprint import pprint

first_arr = np.arange(12).reshape(3,4)
second_arr = np.arange(12)

pprint(first_arr)
pprint(np.transpose(first_arr))

pprint(second_arr[7:3:-1])
pprint(first_arr[:,1])