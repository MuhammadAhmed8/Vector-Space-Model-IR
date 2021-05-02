import os
import string
import nltk
import re
from nltk.corpus import wordnet
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
lemmatizer = WordNetLemmatizer()


def parse():
    """
        The parse function runs through all the documents in the corpus
        and parse it by cleaning, replacing, removing stop-words, and
        tokenizing them.
    """

    global directory
    global total_docs

    for docId in range(1, total_docs + 1):
        doc_name = directory + "{}.txt".format(docId)
        doc = open(doc_name, 'r')
        doc_stream = doc.read()
        doc_stream = re.sub(r'\b-\b', '', doc_stream.lower())
        doc_stream = re.sub(r'[^a-z1-9]+', ' ', doc_stream.lower())

        tokens = tokenize(doc_stream)
        terms = process_tokens(tokens)

        for (term, pos) in terms:
            term = lemmatize_token([term])
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


# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_token(tokens):
    # tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(tokens)

    # tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []

    for word, tag in wordnet_tagged:
        if tag is None:
            # if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            # else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))

    return " ".join(lemmatized_sentence)


def test():
    # *** Test code ***

    parse()
    print(index.dictionary)


if __name__ == "__main__":
    test()
