
"""
    This module deals with computing relevance score using cosine similarity
    between query vector and doc vector. Alpha value = 0.005 by default.
"""


def rank_by_cosine_similarity(index, q_terms, q_vec, total_docs):
    """
        Fast cosine similarity calculation using index and
        Term at a Time scoring.
    """

    scores = dict.fromkeys(range(total_docs+1), 0)
    print(scores)
    ranking = []

    for t, qw in q_vec.items():
        v = index.get_value(t)

        if not bool(v):
            continue

        postings = v['postings']
        weights = v['weights']  # tf_idf scores for term qi for the docs in postings
        print("posting:", postings)
        print("weights:", weights)
        for j, doc in enumerate(postings):
            scores[doc] += weights[j]*qw

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
