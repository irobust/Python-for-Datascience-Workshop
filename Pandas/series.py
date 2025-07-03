import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    column_names = ['Year', 'City', 'Sport', 'Athlete Name', 'Event Gender', 'Medal']
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5).drop('City', axis=1)

    # mapper = {
    #     'Event Gender': 'Gender',
    #     'Athlete Name': 'Name'
    # }

    # oo = oo.rename(columns=mapper)
    
    oo = oo.filter(items=['Year', 'Sport', 'Athlete Name', 'Event Gender'], axis=1)
    # oo = oo.filter(like='Cycling', axis=0)

    pprint(oo[(oo.Year == 1896) & (oo['Event Gender'] == 'M')])

    # pprint(type(oo['Discipline']))
    # pprint(oo['Sport'].unique())
    # pprint(oo['Sport'].value_counts())
    # pprint(oo['Medal'].unique())
    # pprint(oo['Medal'].value_counts())
else:
    print("File not found!")