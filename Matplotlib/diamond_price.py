import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pprint import pprint

diamonds = pd.read_csv("./data/Diamonds Prices2022.csv")

sb.barplot(x="cut", y="carat", data=diamonds)

plt.show()