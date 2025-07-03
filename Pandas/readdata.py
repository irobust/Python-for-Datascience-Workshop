import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5)
    pprint(oo.describe([0.8,0.9]))
    pprint(oo.info())
    pprint(oo.shape)
else:
    print("File not found!")


# mySeries = pd.Series(np.array([1,2,3,4,5]))
# myDataFrame = pd.DataFrame(np.arange(1,11).reshape(5,2))

# pprint(mySeries)
# pprint(myDataFrame)

