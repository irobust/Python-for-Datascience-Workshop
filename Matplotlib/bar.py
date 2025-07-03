import matplotlib.pyplot as plt
from pprint import pprint

plt.bar(
    x = range(1,11),
    height= [x**2 for x in range(1,11)]
)

plt.show()