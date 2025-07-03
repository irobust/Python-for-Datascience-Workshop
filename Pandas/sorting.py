import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5)
    
    # Sorting with Series
    # oo = oo['Athlete Name'].sort_values()

    oo = oo.filter(['Year', 'Sport', 'Athlete Name', 'Gender'], axis=1)
    # Sorting with DataFrame
    # oo = oo.sort_values('Athlete Name', ascending=False)

    oo = oo.sort_values(by=['Year','Athlete Name'], ascending=[False, True])

    pprint(oo)