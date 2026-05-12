from retrieval.vector_search import (
    vector_search
)

from reasoning.reasoning_engine import (
    generate_reasoning_answer
)


class QueryAgent:

    def __init__(self):

        self.available_sources = [
            "slack",
            "meeting",
            "support_ticket",
            "crm"
        ]

    def decide_sources(
        self,
        question
    ):

        lowered = question.lower()

        selected_sources = []

        if (
            "customer" in lowered
            or "enterprise" in lowered
            or "deal" in lowered
        ):

            selected_sources.extend([
                "crm",
                "support_ticket"
            ])

        if (
            "deployment" in lowered
            or "incident" in lowered
            or "outage" in lowered
            or "engineering" in lowered
        ):

            selected_sources.extend([
                "slack",
                "meeting"
            ])

        if not selected_sources:

            selected_sources = (
                self.available_sources
            )

        return list(
            set(selected_sources)
        )

    def retrieve_memories(
        self,
        question,
        sources
    ):

        all_memories = []

        for source in sources:

            results = vector_search(
                query=question,
                source_filter=source
            )

            all_memories.extend(results)

        return all_memories

    def answer_question(
        self,
        question
    ):

        selected_sources = (
            self.decide_sources(
                question
            )
        )

        memories = (
            self.retrieve_memories(
                question,
                selected_sources
            )
        )

        answer = (
            generate_reasoning_answer(
                question,
                memories
            )
        )

        formatted_memories = []

        for memory in memories:

            formatted_memories.append({
                "score": memory.score,
                "content": memory.payload.get(
                    "content",
                    ""
                ),
                "metadata": memory.payload.get(
                    "metadata",
                    {}
                )
            })

        return {
            "selected_sources": (
                selected_sources
            ),
            "answer": answer,
            "evidence": (
                formatted_memories
            )
        }