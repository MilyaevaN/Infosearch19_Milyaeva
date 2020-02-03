from pymorphy2 import MorphAnalyzer
from pymorphy2.tokenizers import simple_word_tokenize
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
stops = stopwords.words("russian")

f = open('sents.txt', 'r', encoding = 'utf-8')
sents = f.readlines()
f.close()

m = MorphAnalyzer()
def normalize_text(text):
    lemmas = []
    for t in simple_word_tokenize(text):
        if t not in stops:
            lemmas.append(m.parse(t)[0].normal_form)
    return ' '.join(lemmas)
