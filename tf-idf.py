import os
import re
import nltk
from nltk import ngrams
from nltk.text import Text
import pymorphy2 as pm2
pmm = pm2.MorphAnalyzer()
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
import numpy as np
from collections import OrderedDict

nltk.download("stopwords")
from nltk.corpus import stopwords
rus_stopwords = stopwords.words("russian")

def make_texts()
    texts = []
    f = open('C:\Сохраненное\Комп.линг\project\quora_question_pairs_rus.csv', 'r', encoding = 'utf-8')
        for line in f:
        text = [pmm.normal_forms(x)[0] for x in line.split() if x not in rus_stopwords]
        texts.append(text)
    return texts
    
def make_words (texts):
    vect_texts = vectorizer.fit_transform(texts)
    matrix = vect_texts.toarray()
    inv_matrix = np.transpose(matrix)
    words = vectorizer.get_feature_names()
    return words, inv_matrix
    
def n_search(words, inv_matrix, query):    
    q_norm = [pmm.normal_forms(x)[0] for x in query.split() if x not in rus_stopwords]
    n = []
    for word in words:
        if word in q_norm:
            n.append(1)
        else:
            n.append(0)
    ans = []
    for i in range():
        count = 0
        x = inv_matrix[:,i]
        for j in range():
            if n[j] == 1 and x[j] != 0:
                count += 1
        ans.append(count)
    answer = dict(zip(ans))
    sorted_answer = OrderedDict(sorted(final.items(), key=lambda kv: kv[1], reverse=True))
    for key, value in sorted_final.items():
    final_answer = key
    return final_answer
    
