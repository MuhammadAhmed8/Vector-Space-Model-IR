import math


def tf(freq):
    return math.log(freq, 10) + 1


def idf(d_freq, total_docs):
    return math.log(total_docs / d_freq, 10)


def apply_weighting_scheme(index, total_docs):
    for k, v in index.get_items():
        v['idf'] = idf(len(v['postings']), total_docs)
        tfs = v['tfs']

        for i, freq in enumerate(tfs):
            tfs[i] = tf(freq)
            tfs[i] *= v['idf']


def find_vectors_magnitudes(index, total_docs):
    magnitudes = [] * total_docs

    for k, v in index.get_items():
        for i, doc in enumerate(v['postings']):
            magnitudes[doc] += v['tfs'] ** 2

    return [math.sqrt(m) for m in magnitudes]

