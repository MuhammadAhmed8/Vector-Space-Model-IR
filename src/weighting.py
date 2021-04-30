import math


def tf(freq):
    return freq


def idf(d_freq, total_docs):
    return math.log(total_docs/d_freq)


def apply_weighting_scheme(index, total_docs):

    for k, v in index.get_items():
        v['idf'] = idf(len(v['postings']), total_docs)
        weights = v['weights']

        for i, w in enumerate(weights):
            weights[i] = tf(w) * v['idf']       # calculating tf-idf weights.


def find_vectors_magnitudes(index, total_docs):

    magnitudes = [0]*(total_docs+1)

    for k, v in index.get_items():
        for i, doc in enumerate(v['postings']):
            magnitudes[doc] += (v['weights'][i] ** 2)

    return [math.sqrt(m) for m in magnitudes]


def normalize_weights(index, magnitudes):

    for k, v in index.get_items():
        for i, doc in enumerate(v['postings']):
            v['weights'][i] /= magnitudes[doc]


def get_query_vector(index, query):

    q_vec = []
    magnitude = 0

    for i, t in enumerate(query):
        q_vec.append(index.get_value(t)['idf'])
        magnitude += q_vec[-1]**2

    magnitude = math.sqrt(magnitude)

    return [q/magnitude for q in q_vec]