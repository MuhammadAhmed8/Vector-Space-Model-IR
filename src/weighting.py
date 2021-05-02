import math


def tf(freq):
    return freq

def log_tf(freq):
    return 1 + math.log(freq)

def idf(d_freq, total_docs):
    return math.log(total_docs/d_freq)


def calculate_tf_idf(index, total_docs):

    for k, v in index.get_items():
        v['idf'] = idf(len(v['postings']), total_docs)
        weights = v['weights']

        for i, w in enumerate(weights):
            weights[i] = tf(w) * v['idf']      # calculating tf-idf weights.


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


def get_query_vector(index, q_terms):

    q_vec = {}
    magnitude = 0

    for i, t in enumerate(q_terms):
        if t not in q_vec:
            q_vec[t] = 1
        else:
            q_vec[t] += 1



    for t, c in q_vec.items():
        value = index.get_value(t)
        if bool(value):
            w = c
            q_vec[t] = w
            magnitude += w**2
        else:
            q_vec[t] = 0

    magnitude = math.sqrt(magnitude)


    if magnitude == 0:
        return q_vec

    for t, q in q_vec.items():
        q_vec[t] = q/magnitude

    return q_vec


