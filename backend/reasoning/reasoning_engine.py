from llm.llm_client import (
    generate_text
)


def generate_reasoning_answer(
    question,
    memories
):

    combined_context = ""

    for memory in memories:

        combined_context += (
            memory.payload.get(
                "content",
                ""
            )
            + "\n"
        )

    prompt = f"""
    You are an organizational intelligence AI.

    Answer the question using the provided organizational memories.

    Question:
    {question}

    Organizational Memories:
    {combined_context}

    Instructions:
    - Give a concise answer
    - Summarize findings clearly
    - Use at most 5 lines
    - Synthesize information
    - Do not repeat duplicate memories
    """

    response = generate_text(
        prompt
    )

    return response