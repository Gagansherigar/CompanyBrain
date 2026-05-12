from retrieval.vector_search import (
    vector_search
)

from reasoning.root_cause_analysis import (
    analyze_root_cause
)

events = vector_search(
    "outage"
)

result = analyze_root_cause(
    events
)

print(result)