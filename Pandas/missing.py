import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5)

    oo.dropna(how="any", axis=0)
    pprint(oo.duplicated().unique())
    
    pprint(oo.loc[oo.duplicated(),:])
    oo = oo.drop_duplicates()

    pprint(oo.duplicated().unique())
    print(oo.Event.isna().unique())

    pprint(oo.iloc[16139])