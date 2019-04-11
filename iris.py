# Ian Wafer
# 02/04/2019

# Code to be created- Min & max of each column, average of each column, typical deviation from average.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')

plt.scatter(iris['sepal_length'], iris['sepal_width'], iris['petal_width'], iris['petal_length'])

plt.show()

# https://stackoverflow.com/questions/42777946/plotting-from-dataset-in-python