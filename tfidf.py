from typing import Dict, Any, Union, List, Tuple
from functools import reduce
from math import log10
from re import subn
from pprint import pprint
from collections import OrderedDict


def tf(word: str, doc: List[str], cache_tf: Union[Dict, None]) -> float:
    try:
        return cache_tf[word]
    except (KeyError, TypeError):
        res = doc.count(word)/len(doc) if len(doc) else 0
        if cache_tf:
            cache_tf[word] = res
        return res


def idf(word: str, docs: Dict[Any, List[str]], cache_idf: Union[Dict, None]) -> float:
    try:
        return cache_idf[word]
    except (KeyError, TypeError):
        count = reduce(lambda cnt, doc: cnt + int(word in doc), docs.values(), 0)
        res = log10(len(docs)/count) if count else 0
        if cache_idf:
            cache_idf[word] = res
        return res


def document_preflight(doc: str) -> List[str]:
    doc = doc.lower().split()
    doc = map(lambda word: subn(r"^\W*([a-z-]+?)\W*$", r"\g<1>", word), doc)
    doc = [res[0] for res in doc if res[1] and len(res[0])]
    # TODO: Add stopwords
    return doc


def tf_idf(docs: Dict[Any, str]) -> Dict[str, Dict[Any, float]]:
    cache_tf = {}
    cache_idf = {}
    docs = {i: document_preflight(doc) for i, doc in docs.items()}
    res = {}  # res[word][doc_ndx]

    for i, doc in docs.items():
        for word in doc:
            res.setdefault(word, {})[i] = tf(word, doc, cache_tf) * \
                                          idf(word, docs, cache_idf)

    for i, vec in res.items():
        res[i] = OrderedDict(sorted(vec.items(), key=lambda x: -x[1]))

    return res


def search(word, index) -> Union[List[Tuple[int, int]], None]:
    try:
        return index[word]
    except KeyError:
        return None


##index = tf_idf({
##    0: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
##         'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
##    1: 'Wikipedia ((About this soundlisten) wik-ih-PEE-dee-ə or '
##         '(About this soundlisten) wik-ee-PEE-dee-ə) is a multilingual '
##         'online encyclopedia created and maintained as an open collaboration project[4] '
##         'by a community of volunteer editors using a wiki-based editing system.[5]',
##    2: 'Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[14] '
##         'Sanger coined its name,[15][16] as a portmanteau of "wiki" (the Hawaiian word for '
##         '"quick"[17]) and "encyclopedia". Initially an English-language encyclopedia, versions '
##         'of Wikipedia in other languages were quickly developed.',
##    3: 'Python is an interpreted, high-level, general-purpose programming language. Created by '
##         'Guido van Rossum and first released in 1991, Python\'s design philosophy emphasizes code '
##         'readability with its notable use of significant whitespace. Its language constructs and '
##         'object-oriented approach aim to help programmers write clear, logical code for small and '
##         'large-scale projects.[28] ',
##})
##
##pprint(index)
##try:
##    while True:
##        word = input('Search word: ')
##        res = search(word, index)
##        if not res:
##            print('Word not found')
##            continue
##        print('Index    Correlate')
##        for i in res:
##            print(f'{i:<8} {res[i]:3e}')
##except KeyboardInterrupt:
##    pass
