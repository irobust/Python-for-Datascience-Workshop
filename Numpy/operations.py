import numpy as np
from pprint import pprint

first_arr = np.arange(1,3)
second_arr = np.arange(11,21).reshape(5,2)


third_arr = second_arr + first_arr
third_arr = np.add(first_arr, second_arr)

pprint(first_arr)
pprint(second_arr)
pprint(third_arr)