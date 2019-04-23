

# Programming & Scripting GMIT 2019 52445 Python Scripting Project
Ian Wafer

02/04/2019

G00376322


## Fisher Iris Data Set

![Iris Flower](/images/irissetosa(Resized).jpg 'Setosa') ![Iris Flower](/images/irisversicolor(Resized).jpg 'Versicolor') ![Iris Flower](/images/irisvirginica(Resized).jpg 'Virginica') 

  

## Project Description

This is a project set out by Ian Mcloughin for the programming and scripting module number 52445.  It entails reseaching the Fisher Iris data set and then writing documentation and code in the python programming language based on that research. It is expected to break the project down into smaller tasks and treat it as if we are to explain to out work colleagues what the data set investigation has shown.

The instructions issued to us can be found here- [link](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## Introduction

The Iris data set is a well known database in pattern recognition originally created by R.A. Fisher and published in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is a multivariate collection of four attributes for 3 variations of the Iris flowers. The attributes it covers are the length and width of the sepal and the length and width of the petal in four sperate columns and each row is associated with one of the 3 class' of the Iris plant. 

The Iris classes covered are the [Iris Setosa](https://en.wikipedia.org/wiki/Iris_setosa), the [Iris Versicolor](https://en.wikipedia.org/wiki/Iris_versicolor) and the [Iris Virginica](https://en.wikipedia.org/wiki/Iris_virginica). Each class of plant has 50 instances of measurements taken in the data set. 

The instructions can be found here- [link](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

### How to download this repository
1. Go to Github profile located here- [link](https://github.com/IanWafer)
2. Click repository labeled IanWafer/Fisher-Iris_Data_Set.
3. Click the download button or clone th repository to your own Github account.

### How to run the code.
1. Install a python code client (Anaconda recommended. See here for installer- [link](https://www.anaconda.com/distribution/)
2. Run a command line client (cmder recommended. See here for installer- [link](https://github.com/cmderdev/cmder/releases/download/v1.3.11/cmder.zip)
3. Ensure you are in the correct directory where each python script is located using the cd command to navigate.
4. Run the python script by typing iris.py

## Initial Data Review

Initially on my review I first imported the modules required to run the analysis of the data set as shown below-

![Imported Modules](/images/ImportedModules.png)

With the required modules imported the read file function was shorted to make it more user friendly in code design and the first ten lines read and output as shown below using the .head() function-

![Iris Read](/images/IrisRead.png)

![Iris Head](/images/IrisHead.png)

The size of each grouping broken down by species was then determined using the groupby and size function together shown below with results displyed below the code-

![Iris Group By Size](/images/IrisGroupBySize.png)

![Iris Group By Size Results](/images/IrisGroupBySizeResults.png)

Follwing this some quick statistics of the overall data set and dimensions was determined using the .describe function and transposed to display a horizontal table-

![Iris Describe](/images/IrisDescribe.png)

This is then further broken down by species shown below-

![Iris Species Describe](/images/IrisSpeciesDescribe.png)

## Visualisation Of Data

## Findings



Bibliography

https://archive.ics.uci.edu/ml/datasets/iris
https://www.kaggle.com/mjbahmani/20-ml-algorithms-15-plot-for-beginners
https://www.kaggle.com/aschakra/iris-data-visualization-using-python