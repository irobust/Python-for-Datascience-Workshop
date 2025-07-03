import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from pprint import pprint

data = np.random.normal(size=1000)

sb.displot(data, kind='kde')

plt.show()
