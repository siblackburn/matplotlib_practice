import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#names the columns in the csv file
iris = pd.read_csv('iris\iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

wine_reviews = pd.read_csv('iris\winemag-data-130k-v2.csv', index_col=0)

#using pandas for a scatter plot
iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
plt.show()

#line chart with legend (class)
iris.drop(labels=['class'], axis=1).plot.line(title="iris data")
plt.show()


#histogram
wine_reviews['points'].plot.hist()
plt.show()
#multiple histograms. Layout=number of rows and columns
iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)
plt.show()


#bar chart. Count the occurrences a certain number of points has occurred, then sort in order
wine_reviews['points'].value_counts().sort_index().plot.bar()
plt.show()
#horizontal bars
wine_reviews['points'].value_counts().sort_index().plot.barh()
plt.show()

# bar chart grouped by country column. Then average price is taken, and the 5 countries with the highest ave price is shown
wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()