from reasoning.reasoning_engine import (
    generate_reasoning_answer
)


def reason(
    question,
    memories
):

    return generate_reasoning_answer(
        question,
        memories
    )