# Ian Wafer
# 02/04/2019

# Code to be created- Min & max of each column, average of each column, typical deviation from average.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv("input\iris.csv")

sns.set(style="ticks")
g = sns.relplot(x="sepal_length", y="sepal_width", hue="species", palette=["b", "r", "g"], col="species", data=iris)


plt.subplots_adjust(top=0.85)
g.fig.suptitle("Test")

h = sns.relplot(x="sepal_length", y="sepal_width", hue="species", palette=["b", "r", "g"], data=iris)

# The below adds a title to the combined flower output chart
h.fig.suptitle("Overlapping Species Sizes")

plt.show()
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# https://stackoverflow.com/questions/54209895/seaborn-relplot-how-to-control-the-location-of-the-legend-and-add-title