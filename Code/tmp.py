from multiprocessing import Pool
import pandas as pd
import pickle
import threading
from Levenshtein import distance as lev
import itertools
from sklearn.cluster import DBSCAN
import json
import sys
import dateutil
import pkg_resources
import numpy as np
from dateutil.relativedelta import relativedelta
from datetime import datetime
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import argparse
from tqdm import tqdm

from functools import lru_cache, partial
lru_cache = lru_cache(maxsize=None)

#2
def tokenizer(text):
    return text.split(' ')

#3
@lru_cache
def jaccard(x, y):
    """
    To tokenize text and compute jaccard disatnce
    """
    x_w = set(tokenizer(x))
    y_w = set(tokenizer(y))
    return (
        len(x_w.symmetric_difference(y_w)) / (len(x_w.union(y_w)) if len(x_w.union(y_w)) > 0 else 1)
    )
#4
@lru_cache
def levenshtein(x, y, n=None):
    if n is not None:
        x = x[:n]
        y = y[:n]
    return lev(x, y) / (max(len(x), len(y)) if max(len(x), len(y)) > 0 else 1)

#5
def average_jac_lev(x, y):
    """
    Computes average of jacard and levenshtein for 2 given strings
    """
#     print('entered jaccard')
    return (jaccard(x, y) + levenshtein(x, y)) / 2
#6
def compute_distance(items, distance):
    """
    Computes a distance matrix for given items, using given distance function.
    """
    m = np.zeros((len(items), len(items)))
    enumitems = list(enumerate(items))
    for xe, ye in itertools.combinations(enumitems, 2):
        i, x = xe
        j, y = ye
        d = distance(x, y)
        m[i, j] = m[j, i] = d
    return m


def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    if len(array) == 0:
        return 0
    array = array.flatten()
    if np.amin(array) < 0:
        array -= np.amin(array)
    array += 0.0000001
    array = np.sort(array)
    index = np.arange(1, array.shape[0] + 1)
    n = array.shape[0]
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array)))

def task(data):
    """
    Threading and Progress
    """
#     print('entered task')
    author, group, max_comments, params = data
    group = group[:max_comments]
    clustering = DBSCAN(eps=params['eps'], min_samples=1, metric='precomputed')
    items = compute_distance(getattr(group, params['source']), params['func'])
    clusters = clustering.fit_predict(items)
    empty_comments = np.count_nonzero(group['empty'])

    return (
        author,
        len(group),
        empty_comments,
        len(np.unique(clusters)),
        gini(items[np.tril(items).astype(bool)]),
    )