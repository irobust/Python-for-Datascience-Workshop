import numpy as np
from pprint import pprint

first_arr = np.arange(10, 110, 10)
second_arr = first_arr.copy().reshape(2,5)
third_arr = np.array([[1,1,5,2,2],[1,1,5,2,2],[1,3,3,2,2],[1,1,3,2,2]])

pprint(first_arr.sum())
pprint(second_arr)
pprint(second_arr.sum(axis=1))

pprint(np.average(first_arr))
pprint(np.std(first_arr))
pprint(np.unique(third_arr, axis=0))