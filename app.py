from tfidf import search, tf_idf
from flask import Flask, render_template_string, request

def make_data():
    f = open('cl.sents.txt', 'r', encoding = 'utf-8')
    texts = f.readlines()
    f.close()
    docs = {}
    i = 0
    for el in texts:
       docs[i] = el
       i = i+1
    return docs

docs = make_data()
index = tf_idf(docs)

def make_data2():
    f = open('sents.txt', 'r', encoding = 'utf-8')
    texts = f.readlines()
    f.close()
    docs2 = {}
    i = 0
    for el in texts:
       docs2[i] = el
       i = i+1
    return docs2

docs2 = make_data2()

app = Flask(__name__)

@app.route('/')
def main():
    word = request.args.get('q')
    if not word:
        return render_template_string('<form><input name="q" /><button>Search</button></form>')
    res = search(word, index)
    if not res:
        return render_template_string('Word not found')
    return render_template_string(
        '<table>'
        '<tr><th>Index</th><th>Correlate</th><th>Document</th></tr>'
        '{%for i in res%}'
        '<tr><td>{{i}}</td><td>{{res[i]}}</td><td>{{docs2[i]}}</td></tr>'
        '{%endfor%}</table>', res=res, index=index, docs2=docs2)
 
app.run()
