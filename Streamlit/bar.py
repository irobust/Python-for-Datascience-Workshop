import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

animals = ['Cat', 'Dog', 'Rabbit']
height = [30, 80, 50]
width = [5, 40, 30]

x = np.arange(len(animals))

fig, ax = plt.subplots()

ax.bar(x, height, 0.4, color='red')
ax.bar(x, width, 0.4, color="orange")
ax.legend('height', 'width')

st.pyplot(fig)