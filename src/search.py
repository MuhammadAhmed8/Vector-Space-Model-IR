"""
    Author = Muhammad Ahmed
    Run this file to test the code on console
    or run the gui file
"""

import re

from nltk import WordNetLemmatizer
from inverted_index import InvertedIndex
from inverted_index import PositionalInvertedIndex
from ranking import *
from weighting import *

index = {}
pos_index = {}


def load_index():

    # Load inverted index from disk.

    global index
    global pos_index
    index = InvertedIndex()
    index.read_index()
    pos_index = PositionalInvertedIndex()
    pos_index.read_index()

# Result : 3 8 10 15 17 20 21 23 27 28 29 43 48 49

def process_query(query):

    # A wrapper function which takes the raw query,
    # identifies it's type, and cleans the query.

    lemmatizer = WordNetLemmatizer()
    q_vec = query.split()
    for (i, q) in enumerate(q_vec):
        q = q.replace('-', '')
        q = re.sub(r'[^a-z1-9]+', '', q.lower())
        q_vec[i] = lemmatizer.lemmatize(q)

    return q_vec


def find_relevant_docs(q_terms):
    q_vec = get_query_vector(index, q_terms)
    print(q_vec)
    return rank_by_cosine_similarity(index, q_terms, q_vec, 50)


def run_free_text_search(query):

    q_terms = process_query(query)
    print(q_terms)
    docs = find_relevant_docs(q_terms)
    print(docs)

    for k in docs:
        if k[1] >= 0.005:
            print(k[0], end=" ")


if __name__ == "__main__":

    # Test code from console. There is a gui as well.

    print("loading....")
    load_index()
    query = input("Enter query: ")
    run_free_text_search(query)
