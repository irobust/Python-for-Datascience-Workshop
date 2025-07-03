import matplotlib.pyplot as plt
import pandas as pd

data = [x**3 for x in range(10)]

s = pd.Series(data)

plt.plot(s)
plt.show()