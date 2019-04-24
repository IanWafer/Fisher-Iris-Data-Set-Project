

# Programming & Scripting GMIT 2019 52445 Python Scripting Project
Ian Wafer

02/04/2019

G00376322


## Fisher Iris Data Set

![Iris Flower](/images/irissetosa(Resized).jpg 'Setosa') ![Iris Flower](/images/irisversicolor(Resized).jpg 'Versicolor') ![Iris Flower](/images/irisvirginica(Resized).jpg 'Virginica') 

  

## Project Description

This is a project set out by Ian Mcloughin for the programming and scripting module number 52445.  It entails reseaching the Fisher Iris data set and then writing documentation and code in the python programming language based on that research. It is expected to break the project down into smaller tasks and treat it as if we are to explain to out work colleagues what the data set investigation has shown.

The instructions issued to us can be found here- [link](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## Table of Contents

1. [Introduction](#introduction)

2. [Initial Data Review](#initialreview)

3. [Visualisation Of Data](#visualisation)

    3.1 [Histogrmas](#hist)

    3.2 [Violinplots](#vio)

    3.3 [Pairplot](#sca)

4. [Concluding Remarks](#conc)

5. [Bibliogrpahy](#bibliography)

<a name="introduction"></a>
## 1. Introduction 

The Iris data set is a well known database in pattern recognition originally created by R.A. Fisher and published in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is a multivariate collection of four attributes for 3 variations of the Iris flowers. The attributes it covers are the length and width of the sepal and the length and width of the petal measured in centimeters in four sperate columns and each row is associated with one of the 3 class' of the Iris plant. 

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

<a name="initialreview"></a>

## 2. Initial Data Review 

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

From this data it's clear the petal length is a clear outlier for idetying the Iris Setosa flower type. With further investigation we can determine more features to identify the correct flower type.

<a name="visualisation"></a>

## 3. Visualisation Of Data

<a name="hist"></a>

### 3.1 <u>Histograms</u>
From the histogram plot we can compare the quantites of each flower petal and sepal dimension to deterimine the realitive density of the values. From this we can see that the flower sepals have a lot of overlap. While overlap still exists between the virginica and versicolour petal sizes, it would still be a much greater method of identification between the different flower types as a unique idetifier. As we can see below the Setosa flower is very clearly distinguished from the virginica and versicolour flowers being a much smaller petal size. As we can see below this does not carry over to the sepal. From the 2 sepal grpahs below we can see that while the sepal might be short in length it has a larger width in most cases compared to the virginica and versicolour plants.

![Histo Petal Length](/images/Outputs/Hist-Petal_Length.png)

![Histo Petal Width](/images/Outputs/Hist-Petal_Width.png)

![Histo Sepal Length](/images/Outputs/Hist-Sepal_Length.png)

![Histo Sepal Width](/images/Outputs/Hist-Sepal_Width.png)

<a name="vio"></a>

### 3.2 <u>Violinplots</u>

The violin plot is a method of graphically depicting numerical data through their quartiles with a rotated kernal density plot on each side. They can be used for showing the probability density at different values showing a full distribution of the data. This shows us the typical ranges of the petal and sepal dimensions with any great number of clustered values giving a greater visula impact through the larger dimension shown on the plot.

![Violin Petal Length](/images/Outputs/Violin-Petal_Length.png)

![Violin Petal Width](/images/Outputs/Violin-Petal_Width.png)

![Violin Sepal Length](/images/Outputs/Violin-Sepal_Length.png)

![Violin Sepal Width](/images/Outputs/Violin-Sepal_Width.png)

<a name="sca"></a>

### 3.3 <u>Pairplot</u>

Scatterplots are used for displaying information across three variables with colour coding for a data set. From the below images you can clearly see the setosa plant can be seperated and easily identified using its petal dimensions. This is not as clear cut for the versicolour and virginica though as there is considerable overlap even if we do see that the virginica does trend toward the larger size petal and sepal.

![Pair Plot](/images/Outputs/pairplot.png)

<a name="conc"></a>

## 4. Concluding Remarks

The Iris Dataset was used to give me a broad understanding of a multitude of features for analysing and gaining statistical information from a set of data. I discovered how to use a number of features from the pandas, numpy, seaborn and matplotlib libraries. I used functions to determine a breakdown of the information, the average of the columns, the standard deviations, min and max values. I also learned to use numerous chart types and how to manipulate the grpahs, labels etc. to visualise the data in a suitable manner. 

<a name="bibliography"></a>

## 5. Bibliography

Archive.ics.uci.edu. (2019). UCI Machine Learning Repository: Iris Data Set. [online] Available at: https://archive.ics.uci.edu/ml/datasets/iris 

 Kaggle.com. (2019). +20 ML Algorithms +15 Plot for Beginners | Kaggle. [online] Available at: https://www.kaggle.com/mjbahmani/20-ml-algorithms-15-plot-for-beginners.

Kaggle.com. (2019). Iris Data Visualization using Python | Kaggle. [online] Available at: https://www.kaggle.com/aschakra/iris-data-visualization-using-python.

Seaborn.pydata.org. (2019). Controlling figure aesthetics — seaborn 0.9.0 documentation. [online] Available at: https://seaborn.pydata.org/tutorial/aesthetics.html.

Seaborn.pydata.org. (2019). seaborn.FacetGrid — seaborn 0.9.0 documentation. [online] Available at: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html.

title, s. (2019). seaborn relplot: how to control the location of the legend and add title. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/54209895/seaborn-relplot-how-to-control-the-location-of-the-legend-and-add-title.

Seaborn.pydata.org. (2019). seaborn.swarmplot — seaborn 0.9.0 documentation. [online] Available at: https://seaborn.pydata.org/generated/seaborn.swarmplot.html [Accessed 24 Apr. 2019].

Kaggle.com. (2019). Iris Data Set | Kaggle. [online] Available at: https://www.kaggle.com/willvegapunk/iris-data-set.

GitHub. (2019). Violins out of alignment · Issue #1007 · mwaskom/seaborn. [online] Available at: https://github.com/mwaskom/seaborn/issues/1007 [Accessed 24 Apr. 2019].

Seaborn.pydata.org. (2019). seaborn.distplot — seaborn 0.9.0 documentation. [online] Available at: https://seaborn.pydata.org/generated/seaborn.distplot.html.

Python, R, and Linux Tips. (2019). How To Make Histogram in Python with Pandas and Seaborn?. [online] Available at: http://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/.