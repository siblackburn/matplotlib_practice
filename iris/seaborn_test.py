import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


iris = pd.read_csv('iris\iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
wine_reviews = pd.read_csv('iris\winemag-data-130k-v2.csv', index_col=0)

#scatterplot. Dataset is defined in the body unlike pandas. still need matplotlib to call show function. hue colour codes according to legend
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='class')



# sns.lineplot(data=iris.drop(['class'], axis=1))

#strip plot
# x=iris.petal_length
# y=iris.petal_width
# scatter_plot_attempt = sns.stripplot(x, y)
# scatter_plot_attempt.set(xlabel='petal length', ylabel='petal width')
# plt.title("petals rule")
# plt.show()

#barplot
#sns.countplot(wine_reviews['points'])

# # swarmplot
# sns.swarmplot(x="class", y="petal_length", data=iris)
# plt.show()

#jointplot. reg denotes we want a regression overlaid on top of the graph
# sns.jointplot(data=iris, x='petal_length', y='sepal_length', kind='reg', color='g')
# plt.show()

#heatmap
# df = wine_reviews.pivot_table(index='random', columns='country', values='points', aggfunc=np.median)
# sns.heatmap(df, annot=True, fmt=".1f")
# plt.show()

# heatmap plot showing statistical correlations between variables! Will only accept numerical columns
# sns.heatmap(wine_reviews.corr(), annot=True, fmt=".2f")
# plt.show()

#box and whisker. First define data and distribution. First data=x axis, second=y. Then call boxplot and the data
# df = wine_reviews[(wine_reviews['points']>=95) & (wine_reviews['price']<1000)]
# sns.boxplot('points', 'price', data=df)
# plt.show()


