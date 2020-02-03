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
    doc = map(lambda word: subn(r"^\W*([a-zа-яё-]+?)\W*$", r"\g<1>", word), doc)
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
