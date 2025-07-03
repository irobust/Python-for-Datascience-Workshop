import pandas as pd
import numpy as np
from pprint import pprint
from pathlib import Path

if Path("olympics_1896_2004.csv").exists():
    medal_order = ['Gold', 'Silver', 'Bronze']
    medal_categories = pd.CategoricalDtype(categories=medal_order, ordered=True)
    dtype_mapper = {
        'Year': 'int16',
        'Sport': 'string',
        'Discipline': 'string',
        'Event': 'string',
        'Medal': medal_categories
    }
    oo = pd.read_csv("olympics_1896_2004.csv", skiprows=5, dtype=dtype_mapper)

    oo2 = oo.copy()
    oo = oo.filter(['Year', 'Sport', 'Discipline', 'Event', 'Medal'], axis=1)

    oo = oo[(oo.Year == 1896) & (oo.Sport == 'Cycling') & (oo.Discipline == 'Cycling Road')]
    oo = oo.sort_values('Medal', ascending=True)
    
    pprint(oo)
    # pprint(oo.Medal.memory_usage(deep=True))
    # pprint(oo2.Medal.memory_usage(deep=True))