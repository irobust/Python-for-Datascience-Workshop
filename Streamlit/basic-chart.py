import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from pprint import pprint

column_names = ['column 1', 'column 2', 'column 3']
data = pd.DataFrame(np.random.randint(30, size=(10,3)), columns=column_names)

animals = {
    'cat' : 35,
    'dog' : 47,
    'rabbit': 56
}

'line chart'
st.line_chart(data)

'bar chart'
st.bar_chart(data)

'pie chart'
fig, ax = plt.subplots()
ax.pie(x=animals.values(), 
       labels=animals.keys(),
       autopct="%1.2f%%",
       explode=[0, 0.1, 0])
st.pyplot(fig)