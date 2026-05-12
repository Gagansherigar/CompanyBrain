def rank_memories(results):

    ranked_results = sorted(
        results,
        key=lambda x: x.score,
        reverse=True
    )

    return ranked_results