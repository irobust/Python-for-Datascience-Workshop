import numpy as np
from pprint import pprint

first_arr = np.arange(1, 13).reshape(2,6)
# second_arr = np.arange(11, 21).reshape(2,5)

# third_arr = np.concatenate((first_arr, second_arr), axis=1)
# fourth_arr = np.vstack((first_arr, second_arr))

fifth_arr = np.hsplit(first_arr, 3)

pprint(first_arr)
# pprint(second_arr)
# pprint(third_arr)
# pprint(fourth_arr)
pprint(fifth_arr)