import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


iris = pd.read_csv('iris\iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
wine_reviews = pd.read_csv('iris\winemag-data-130k-v2.csv', index_col=0)



test = list(wine_reviews.description)

# Create the wordcloud object https://python-graph-gallery.com/261-custom-python-wordcloud/

# wordcloud = WordCloud(width=480, height=480, max_font_size=20, min_font_size=10).generate(test)
# plt.figure()
# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.margins(x=0, y=0)
# plt.show()
