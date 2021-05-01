
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

    for i, qi in enumerate(q_terms):
        v = index.get_value(qi)

        if not bool(v):
            continue

        postings = v['postings']
        weights = v['weights']  # tf_idf scores for term qi for the docs in postings

        for j, doc in enumerate(postings):
            scores[doc] += weights[j]*q_vec[i]

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
