from retrieval.vector_search import (
    vector_search
)

results = vector_search(
    "Why did outages increase?"
)

for result in results:

    print(result.payload)