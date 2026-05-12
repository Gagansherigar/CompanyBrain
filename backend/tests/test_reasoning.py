from retrieval.retrieval_pipeline import (
    run_retrieval_pipeline
)

from reasoning.reasoning_engine import (
    generate_reasoning_answer
)

question = (
    "Why did engineering discuss ECS migration?"
)

memories = run_retrieval_pipeline(
    question
)

answer = generate_reasoning_answer(
    question,
    memories
)

print(answer)