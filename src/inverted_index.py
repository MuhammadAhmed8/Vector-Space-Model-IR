import json


def doc_id(pl):
    return pl[0]


def positions(pl):
    return pl[1]


class InvertedIndex:
    """
     VSM Inverted Index for satisfying normal free text queries.
     This class builds the index by storing the doc_ids of terms, normalized
     tf_idf weights, and idf scores for each term.
    """

    def __init__(self):
        self.dictionary = dict()
        self.index_file = "inverted_index.json"

    def add_term(self, term, doc):

        if term not in self.dictionary:
            self.dictionary[term] = {'idf': 0, 'postings': [], 'weights': []}

        tfs = self.dictionary[term]['weights']
        plist = self.dictionary[term]['postings']

        if doc not in plist:
            plist.append(doc)
            tfs.append(1)
        else:
            tfs[-1] += 1

    def get_value(self, term):
        return self.dictionary.get(term, {})

    def get_items(self):
        return self.dictionary.items()

    def get_postings_list(self, term):
        if term in self.dictionary:
            return self.dictionary[term]['postings']

        return []

    def get_df(self, term):
        if term in self.dictionary:
            return self.dictionary[term]['idf']

    def read_index(self):
        with open(self.index_file) as file:
            self.dictionary = json.load(file)

    def intersection(self, list_1, list_2):
        """
            returns common docs from two sorted postings list
            by taking intersection between them to support
            AND queries.
        """

        i = 0
        j = 0
        result_docs = []

        while i < len(list_1) and j < len(list_2):
            if list_1[i] < list_2[j]:
                i = i + 1
            elif list_2[j] < list_1[i]:
                j = j + 1
            else:
                result_docs.append(list_1[i])
                i = i + 1
                j = j + 1

        return result_docs

    def union(self, list_1, list_2):

        """
          Joins two sorted postings list by taking union
          between them to support OR queries.
        """

        i = 0
        j = 0
        result_docs = []

        while i < len(list_1) and j < len(list_2):
            if list_1[i] < list_2[j]:
                result_docs.append(list_1[i])
                i = i + 1
            elif list_2[j] < list_1[i]:
                result_docs.append(list_2[j])
                j = j + 1
            else:
                result_docs.append(list_1[i])
                i = i + 1
                j = j + 1

        while i < len(list_1):
            result_docs.append(list_1[i])
            i += 1

        while j < len(list_2):
            result_docs.append(list_2[j])
            j += 1

        print("ss")
        return result_docs

    def invert(self, posting_list):
        all = range(1, 51)
        result = []
        i = 0
        j = 0
        while j < len(all) and i < len(posting_list):
            if posting_list[i] == all[j]:
                i += 1
                j += 1
            elif all[j] > posting_list[i]:
                i += 1
            else:
                result.append(all[j])
                j += 1

        while j < len(all):
            result.append(all[j])
            j += 1

        return result

    def write_index_to_disk(self):
        with open(self.index_file, "w") as write_file:
            json.dump(self.dictionary, write_file)
