import numpy as np
from pprint import pprint

row = 4
column = 4

# first_arr = np.arange(1, 13)

# second_arr = np.empty((row,column), np.int8)
# if(row * column == np.size(first_arr)):
#     second_arr = np.reshape(first_arr, (row, column))

# try:
#     second_arr = np.reshape(first_arr, (row, column))
# except(ValueError):
#     second_arr = np.empty((row, column), np.int8)

# pprint(first_arr)
# pprint(second_arr)

first_arr = np.full((4, 4), 10)
second_arr = first_arr.flatten()
third_arr = first_arr.ravel()

# second_arr[0] = 99
third_arr[0] = 99

pprint(first_arr)
pprint(second_arr)
pprint(third_arr)