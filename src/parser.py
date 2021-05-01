import os
import string
import nltk
import re
from nltk import pos_tag
from inverted_index import *
from weighting import *
from file_utility import *
from nltk.stem import WordNetLemmatizer


# Parse all files in the given directory

directory = '../dataset/ShortStories/'

parsed_docs = []
removal_words = set()

index = InvertedIndex()
total_docs = 50


def parse():
    """
        The parse function runs through all the documents in the corpus
        and parse it by cleaning, replacing, removing stop-words, and
        tokenizing them.
    """

    global directory
    global total_docs

    lemmatizer = WordNetLemmatizer()

    for docId in range(1, total_docs+1):
        doc_name = directory + "{}.txt".format(docId)
        doc = open(doc_name, 'r')
        doc_stream = doc.read()
        doc_stream = re.sub(r'\b-\b', '', doc_stream.lower())
        doc_stream = re.sub(r'[^a-z1-9]+', ' ', doc_stream.lower())

        tokens = tokenize(doc_stream)
        terms = process_tokens(tokens)

        for (term, pos) in terms:

            term = lemmatizer.lemmatize(term)
            index.add_term(term, docId)

        doc.close()

    calculate_tf_idf(index, total_docs)
    magnitudes = find_vectors_magnitudes(index, total_docs)
    normalize_weights(index, magnitudes)
    index.write_index_to_disk()


def tokenize(stream):
    tokens = nltk.word_tokenize(stream)
    return tokens


def process_tokens(tokens):
    """
       Removes the removal words such as stop words, and
       assigning positions to tokens.
    """

    global removal_words

    if len(removal_words) == 0:
        load_removal_words(removal_words)

    revised_tokens = []

    pos = 0
    i = 0
    while pos < len(tokens):
        is_possessive = 0

        # This section does pos tagging to know if "'s" shows possession
        # or it shows contraction, as I am assigning positions to stop words even
        # to stop words which appear as contraction.

        if pos > 0 and tokens[pos] == 's' and 'NN' not in nltk.pos_tag([tokens[pos - 1]])[0][1]:
            tokens[pos] = 'is'

        if pos > 0 and tokens[pos] == 's' and 'NN' in nltk.pos_tag([tokens[pos - 1]])[0][1]:
            is_possessive = 1
            i -= 1

        i += 1

        if is_possessive == 0 and tokens[pos] not in removal_words:
            revised_tokens.append((tokens[pos], i))

        pos += 1

    # returns processed tokens
    return revised_tokens


def test():

    # *** Test code ***

    parse()
    print(index.dictionary)

    word = "beard"


    # normalize test
    # sum = 0
    # for k, v in index.get_items():
    #     for i, doc in enumerate(v['postings']):
    #         if doc == 1:
    #             sum += v['weights'][i]**2
    #
    # print("LENGTH OF DOC 1:", math.sqrt(sum))


if __name__ == "__main__":
    test()
