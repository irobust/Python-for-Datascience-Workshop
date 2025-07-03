import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5)
    # oo = oo['Athlete Name'].str.capitalize()
    oo = oo.filter(['Athlete Name'], axis=1)
    francis = oo['Athlete Name'].str.contains('Francis')
    pprint(oo[francis])

    pprint(dir(oo['Athlete Name'].str))