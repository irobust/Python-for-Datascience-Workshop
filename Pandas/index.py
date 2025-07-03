import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5)

    # Numeric Indexing
    # pprint(oo.iloc[100:111])
    # pprint(oo.iloc[::-1])

    medals_index = pd.CategoricalIndex(oo.Medal, ordered=True, categories=['Gold', 'Silver', 'Bronze'])
    oo = oo.set_index(medals_index)

    print(oo.index)
    pprint(oo.loc[['Gold','Silver'],['Year', 'Discipline', 'Sport']])
