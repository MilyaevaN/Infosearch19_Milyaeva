def make_data():
    f = open('cl.sents.txt', 'r', encoding = 'utf-8')
    texts = f.readlines()
    f.close()
    docs = {}
    i = 0
    for el in texts:
       data[i] = el
       i = i+1
    return docs
