# Ian Wafer
# 02/04/2019

# Code to be created- Min & max of each column, average of each column, typical deviation from average.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Shorten code to read iris data set file
iris = pd.read_csv("input\iris.csv")

# Setup style of graphs to be created. Creat individual graphs species type with breakdown of colour chenged to pallette parameters
sns.set(style="darkgrid")
g = sns.relplot(x="sepal_length", y="sepal_width", hue="species", palette=["b", "r", "g"], col="species", data=iris)

# Lower subplot heading to creat room for overall title and change axis labels
plt.subplots_adjust(top=0.85)
g.fig.suptitle("Individual Flower Sepal Sizes")
g.set_axis_labels('Sepal Length (cm)', 'Sepal Width (cm)')

# Setup second graph with overlapping species on one graph seperated by colour.
h = sns.relplot(x="sepal_length", y="sepal_width", hue="species", palette=["b", "r", "g"], data=iris)

# The below adds a title to the combined flower output chart
h.fig.suptitle("Overlapping Species Sepal Sizes")
h.set_axis_labels('Sepal Length (cm)', 'Sepal Width (cm)')

# Duplicate above for petal dimensions

sns.set(style="darkgrid")
i = sns.relplot(x="petal_length", y="petal_width", hue="species", palette=["b", "r", "g"], col="species", data=iris)

plt.subplots_adjust(top=0.85)
i.fig.suptitle("Individual Flower Petal Sizes")
i.set_axis_labels('Petal Length (cm)', 'Petal Width (cm)')

j = sns.relplot(x="petal_length", y="petal_width", hue="species", palette=["b", "r", "g"], data=iris)

j.fig.suptitle("Overlapping Species Petal Sizes")
j.set_axis_labels('Petal Length (cm)', 'Petal Width (cm)')

plt.show()
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# https://stackoverflow.com/questions/54209895/seaborn-relplot-how-to-control-the-location-of-the-legend-and-add-title