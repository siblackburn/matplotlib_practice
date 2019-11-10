import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#https://www.datacamp.com/community/tutorials/wordcloud-python
#tutorial also shows how to put wordCloud in the shape of an image, or even within colours contained in an image


iris = pd.read_csv('iris\iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
wine_reviews = pd.read_csv('iris\winemag-data-130k-v2.csv', index_col=0)

# print("There are {} observations and {} features in this dataset. \n".format(wine_reviews.shape[0],wine_reviews.shape[1]))
# print("There are {} types of wine in this dataset such as {}... \n".format(len(wine_reviews.variety.unique()),
                                                                        #    ", ".join(wine_reviews.variety.unique()[0:5])))

# country = wine_reviews.groupby("country")
# print(country.describe().head())

# This selects the top 5 highest average points among all 44 countries:
# country.mean().sort_values(by="points",ascending=False).head()


#wordcloud for first description
wine_text = wine_reviews.description[0]

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(wine_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.close()
# wordcloud.to_file("img/first_review.png")


# Create the wordcloud object https://python-graph-gallery.com/261-custom-python-wordcloud/

#wordcloud from the a column of data
text = " ".join(review for review in wine_reviews.description)
print ("There are {} words in the combination of all review.".format(len(text)))


# Create stopword list (they won't appear in results)
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()