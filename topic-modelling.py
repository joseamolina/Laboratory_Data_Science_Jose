""" ------------------- TEST FROM ---------------------------
https://www.toptal.com/python/topic-modeling-python?
utm_campaign=%5BPubs%5D%20Engineering_Newsletter_2022&
utm_medium=email&_hsmi=203516612&_hsenc=p2ANqtz--9O_
iTJAh6THwTC1AYTm8rXigzrUL2c4omM7EEyQRN8bcrqy4CuRDLp7bIxr
E7v9noGXimTA9fH2GaA4dL2fQzLZEY5g&utm_content=203516612&u
tm_source=hs_email
"""

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation as LDA

from nltk.corpus import stopwords
nltk.download('stopwords')

corpus = [ "Rafael Nadal Joins Roger Federer in Missing U.S. Open",
           "Rafael Nadal Is Out of the Australian Open",
           "Biden Announces Virus Measures",
           "Biden's Virus Plans Meet Reality",
           "Where Biden's Virus Plan Stands"]

count_vect = CountVectorizer(stop_words=stopwords.words('english'), lowercase=True)
x_counts = count_vect.fit_transform(corpus)
x_counts.todense()
print(count_vect.get_feature_names())

tfidf_transformer = TfidfTransformer()
x_tfidf = tfidf_transformer.fit_transform(x_counts)

dimension = 2
lda = LDA(n_components=dimension)
lda_array = lda.fit_transform(x_tfidf)
print(lda_array)

components = [lda.components_[i] for i in range(len(lda.components_))]
print(components)
features = count_vect.get_feature_names()
important_words = [sorted(features, key=lambda x: components[j][features.index(x)], reverse = True)[:3] for j in range(len(components))]
print(important_words)


