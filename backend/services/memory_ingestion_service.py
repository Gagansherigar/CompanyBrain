from ingestion.ingestion_pipeline import (
    process_document
)


def ingest_memory_objects(
    memories
):

    for memory in memories:

        process_document(
            text=memory["content"],
            metadata=memory
        )

    return {
        "status": "success",
        "memories_ingested": len(memories)
    }