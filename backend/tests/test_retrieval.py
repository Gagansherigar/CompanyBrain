from retrieval.retrieval_pipeline import (
    run_retrieval_pipeline
)

results = run_retrieval_pipeline(
    "Why did engineering discuss ECS migration?"
)

print(results)