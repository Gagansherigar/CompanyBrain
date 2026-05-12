from retrieval.vector_search import (
    vector_search
)

from retrieval.context_builder import (
    build_context
)

results = vector_search(
    "Kubernetes issues"
)

context = build_context(
    results
)

print(context)