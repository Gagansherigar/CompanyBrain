from retrieval.vector_search import (
    vector_search
)

from memory.memory_ranker import (
    rank_memories
)

results = vector_search(
    "deployment outage"
)

ranked = rank_memories(
    results
)

print(ranked)