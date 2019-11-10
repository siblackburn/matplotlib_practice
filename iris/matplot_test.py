'''
Tutorial: https://towardsdatascience.com/introduction-to-data-visualization-in-python-89a54c97fbed
Matplotlib explanation: https://www.sitepoint.com/plot-charts-python-matplotlib/
Sample data: https://archive.ics.uci.edu/ml/datasets/iris
https://www.kaggle.com/zynicide/wine-reviews
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#names the columns in the csv file
iris = pd.read_csv('iris\iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

# iris_names = pd.read_csv('iris.names', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(iris_names.head())


wine_reviews = pd.read_csv('iris\winemag-data-130k-v2.csv', index_col=0)

# print(wine_reviews.head())


# SCATTERPLOT: create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

#saves the plot. Must be before plt.show
# plt.savefig('first_scatter.png')
#shows you the curent setup
# plt.show()


# create color dictionary
colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(iris['sepal_length'])):
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i],color=colors[iris['class'][i]])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

# plt.show()


# LINE CHART: get columns to plot
columns = iris.columns.drop(['class'])

# create x data
x_data = range(0, iris.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, iris[column])
# set title and legend
ax.set_title('Iris Dataset')
ax.legend(loc='best')
plt.show()




# HISTOGRAM: create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(wine_reviews['points'])
# set title and labels
ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')




# BAR CHART: create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = wine_reviews['points'].value_counts() 
# get x and y data 
points = data.index 
frequency = data.values 
# create bar chart 
ax.bar(points, frequency) 
# set title and labels 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')

# plt.show()



