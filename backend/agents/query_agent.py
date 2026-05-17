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

    def retrieve_memories(
        self,
        question
    ):

        all_memories = []

        for source in self.available_sources:

            try:

                results = vector_search(
                    query=question,
                    source_filter=source
                )

                all_memories.extend(
                    results
                )

            except Exception:

                continue

        all_memories = sorted(
            all_memories,
            key=lambda x: x.score,
            reverse=True
        )

        return all_memories[:12]

    def is_relevant(
        self,
        memories
    ):

        if not memories:

            return False

        high_confidence_count = len([

            memory

            for memory in memories

            if memory.score > 0.18
        ])

        average_score = sum([

            memory.score

            for memory in memories[:5]

        ]) / min(
            len(memories),
            5
        )

        return (
            high_confidence_count >= 2
            or average_score > 0.22
        )

    def build_timeline(
        self,
        memories
    ):

        timeline = []

        sorted_memories = sorted(

            memories,

            key=lambda x: (

                x.payload.get(
                    "metadata",
                    {}
                ).get(
                    "timestamp",
                    ""
                )
            )
        )

        for memory in sorted_memories:

            metadata = memory.payload.get(
                "metadata",
                {}
            )

            timeline.append({

                "timestamp": metadata.get(
                    "timestamp",
                    ""
                ),

                "source": metadata.get(
                    "source",
                    ""
                ),

                "content": memory.payload.get(
                    "content",
                    ""
                )
            })

        return timeline

    def answer_question(
        self,
        question
    ):

        memories = (
            self.retrieve_memories(
                question
            )
        )

        if not memories:

            return {

                "selected_sources": [],

                "answer": (
                    "I could not find relevant "
                    "organizational context."
                ),

                "timeline": [],

                "evidence": []
            }

        is_relevant = (
            self.is_relevant(
                memories
            )
        )

        if not is_relevant:

            return {

                "selected_sources": [],

                "answer": (
                    "This question appears "
                    "outside the organizational "
                    "knowledge base."
                ),

                "timeline": [],

                "evidence": []
            }

        answer = (
            generate_reasoning_answer(
                question,
                memories
            )
        )

        timeline = (
            self.build_timeline(
                memories
            )
        )

        formatted_memories = []

        selected_sources = set()

        for memory in memories:

            metadata = memory.payload.get(
                "metadata",
                {}
            )

            source = metadata.get(
                "source",
                ""
            )

            if source:

                selected_sources.add(
                    source
                )

            formatted_memories.append({

                "score": round(
                    memory.score,
                    4
                ),

                "content": memory.payload.get(
                    "content",
                    ""
                ),

                "metadata": metadata
            })

        return {

            "selected_sources": list(
                selected_sources
            ),

            "answer": answer,

            "timeline": timeline,

            "evidence": (
                formatted_memories
            )
        }