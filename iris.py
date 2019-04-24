# Ian Wafer
# 02/04/2019

# Code to be created- Min & max of each column, average of each column, typical deviation from average.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Shorten code to read iris data set file
iris = pd.read_csv('input\iris.csv')

# Show the first 10 lines of the dataset
print(iris.head(10))

# Print quantity breakdown for amount and type of data by species in csv file
print(iris.groupby('species').size())

# This can be used to give a quick breakdown of all the information by column
print('----------------------Values for all species----------------------')
breakdown = iris.describe()
breakdown = breakdown.transpose()
print(breakdown.head())

# Define category locations
setosa = iris[0:50]
versicolor = iris[50:100]
virginica = iris[100:151]

print('----------------------Iris Setosa Values----------------------')
print(setosa.describe())
print('----------------------Iris Versicolor Values----------------------')
print(versicolor.describe())
print('----------------------Iris Virginica Values----------------------')
print(virginica.describe())

# Plot overlapping histograms of each flower categories properties with axis and labels present
sns.distplot(setosa['sepal_length'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['sepal_length'], color='r', kde=False, label='Versicolor')
sns.distplot(virginica['sepal_length'], color='g', kde=False, label='Virginica')
plt.legend()
plt.xlabel('Sepal Length (cm)')  
plt.ylabel('Quantity')  
plt.savefig('images\Outputs\Hist-Sepal_Length.png')
plt.show()

sns.distplot(setosa['sepal_width'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['sepal_width'], color='r', kde=False, label='Versicolor')
sns.distplot(virginica['sepal_width'], color='g', kde=False, label='Virginica')
plt.legend()
plt.xlabel('Sepal Width (cm)')  
plt.ylabel('Quantity')  
plt.savefig('images\Outputs\Hist-Sepal_Width.png')
plt.show()

sns.distplot(setosa['petal_length'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['petal_length'], color='r', kde=False, label='Versicolor')
sns.distplot(virginica['petal_length'], color='g', kde=False, label='Virginica')
plt.legend()
plt.xlabel('Petal Length (cm)')  
plt.ylabel('Quantity')  
plt.savefig('images\Outputs\Hist-Petal_Length.png')
plt.show()

sns.distplot(setosa['petal_width'], color='b', kde=False, label='Setosa')
sns.distplot(versicolor['petal_width'], color='r', kde=False, label='Versicolor')
sns.distplot(virginica['petal_width'], color='g', kde=False, label='Virginica')
plt.legend()
plt.xlabel('Petal Width (cm)')  
plt.ylabel('Quantity')  
plt.savefig('images\Outputs\Hist-Petal_Width.png')
plt.show()

# Setup for violinplot display with datapoints highlighted in white using swarmplot and print graph 
sns.set(style='darkgrid')
sns.violinplot(x='species', y='sepal_length', palette=['b', 'r', 'g'], data=iris, inner=None)
sns.swarmplot(x='species', y='sepal_length', data=iris, color='white', edgecolor='gray', size=4)
plt.savefig('images\Outputs\Violin-Sepal_Length.png')
plt.show()

sns.violinplot(x='species', y='sepal_width', palette=['b', 'r', 'g'], data=iris, inner=None)
sns.swarmplot(x='species', y='sepal_width', data=iris, color='white', edgecolor='gray', size=4)
plt.savefig('images\Outputs\Violin-Sepal_Width.png')
plt.show()

sns.violinplot(x='species', y='petal_length', palette=['b', 'r', 'g'], data=iris, inner=None)
sns.swarmplot(x='species', y='petal_length', data=iris, color='white', edgecolor='gray', size=4)
plt.savefig('images\Outputs\Violin-Petal_Length.png')
plt.show()

sns.violinplot(x='species', y='petal_width', palette=['b', 'r', 'g'], data=iris, inner=None)
sns.swarmplot(x='species', y='petal_width', data=iris, color='white', edgecolor='gray', size=4)
plt.savefig('images\Outputs\Violin-Petal_Width.png')
plt.show()

sns.pairplot(hue='species', markers='o', data=iris, palette=['b', 'r', 'g'])
plt.savefig('images\Outputs\pairplot.png')
plt.show()

# https://seaborn.pydata.org/tutorial/aesthetics.html
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# https://stackoverflow.com/questions/54209895/seaborn-relplot-how-to-control-the-location-of-the-legend-and-add-title
# https://seaborn.pydata.org/generated/seaborn.swarmplot.html
# https://www.kaggle.com/willvegapunk/iris-data-set
# https://seaborn.pydata.org/generated/seaborn.swarmplot.html
# https://github.com/mwaskom/seaborn/issues/1007
# https://seaborn.pydata.org/generated/seaborn.distplot.html
# http://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/