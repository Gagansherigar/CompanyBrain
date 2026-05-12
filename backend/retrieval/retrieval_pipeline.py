from retrieval.vector_search import vector_search


def run_retrieval_pipeline(query):

    results = vector_search(query)

    return results