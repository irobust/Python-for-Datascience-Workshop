import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

df = pd.DataFrame({
        'x': [x for x in range(10)],
        'y': [x*2 for x in range(10)],
        'z': [x*3 for x in range(10)]
    })

plt.plot(df)
plt.xlabel('List of numbers')
plt.ylabel('Height')
plt.grid()
plt.show()