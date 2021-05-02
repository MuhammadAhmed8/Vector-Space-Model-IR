"""
    Author = Muhammad Ahmed
    Run this file to test the code on console
    or run the gui file
"""

from parser import lemmatize_token
import re
from nltk import WordNetLemmatizer
from ranking import *
from weighting import *
from file_utility import *
from inverted_index import *

index = InvertedIndex()
removal_words = set()
lemmatizer = WordNetLemmatizer()


def init():
    """
        Initializes the system by loading index files and stopwords files.
    """
    global index
    global removal_words

    load_removal_words(removal_words)
    load_index(index)

    """
        This dummy call to lemmatizer preloads the files used by lemmatizer
        on application startup to speed up the query execution.
    """
    lemmatizer.lemmatize("")

def process_query(query):
    """
        A wrapper function which takes the raw query,
        identifies it's type, and cleans the query.
    """

    query = re.sub(r'\b-\b', '', query.lower())
    query = re.sub(r'[^a-z1-9]+', ' ', query.lower())

    q_terms = query.split()

    clean_q_terms = []

    for (i, q) in enumerate(q_terms):

        if q in removal_words:
            continue

        clean_q_terms.append(lemmatize_token([q]))

    return clean_q_terms


def find_relevant_docs(q_terms):
    q_vec = get_query_vector(index, q_terms)

    return rank_by_cosine_similarity(index, q_terms, q_vec, 50)


def run_free_text_search(query, alpha=0.005):
    q_terms = process_query(query)

    docs = find_relevant_docs(q_terms)

    return [d for d in docs if d[1] >= alpha]


if __name__ == "__main__":

    # Test code from console. There is a gui as well.
    init()
    print("loading....")

    while True:
        raw_query = input("Enter query (Type 'x' to quit): ")

        if raw_query == "x":
            break

        alpha_value = float(input("Enter alpha: "))

        result = run_free_text_search(raw_query, alpha_value)
        print("RESULT: ", result)
        print(" ---------------------------------------------------------")

