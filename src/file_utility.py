
"""
    This module is responsible for providing functions
    for loading stop-words, computed indexes, and other
    files from the disk.
"""

# CONFIG VARIABLES
stop_words_filename = "../dataset/Stopword-List.txt"


def load_removal_words(removal_words):
    # loads the stopwords from disk

    with open(stop_words_filename, 'r') as stop_file:
        stop_file_content = stop_file.readlines()

        for word in stop_file_content:
            word = word[:-1].rstrip()
            if word != "":
                removal_words.add(word)


def load_index(index):

    # Load inverted index from disk.
    index.read_index()



