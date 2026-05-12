from services.ingestion_service import (
    ingest_meeting_file
)

from retrieval.retrieval_pipeline import (
    run_retrieval_pipeline
)

from reasoning.reasoning_engine import (
    generate_reasoning_answer
)


# STEP 1
# ingest meeting

ingest_meeting_file(
    "sample_data/meetings/meeting1.txt"
)

print("Meeting ingestion complete")


# STEP 2
# ask organizational question

question = (
    "Why did engineering discuss ECS migration?"
)


# STEP 3
# retrieve memories

memories = run_retrieval_pipeline(
    question
)

print("Retrieved Memories:")
print(memories)


# STEP 4
# generate reasoning answer

answer = generate_reasoning_answer(
    question,
    memories
)

print("\nFinal Answer:\n")
print(answer)