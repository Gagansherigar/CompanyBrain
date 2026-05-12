import uuid

from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text

from llm.embeddings import (
    embedding_model
)

from database.qdrant import (
    qdrant,
    COLLECTION_NAME
)

from qdrant_client.models import (
    PointStruct
)

from reasoning.metadata_extractor import (
    extract_tags,
    classify_memory_type,
    extract_priority
)


def process_document(
    text,
    metadata
):

    cleaned_text = clean_text(text)

    chunks = chunk_text(
        cleaned_text
    )

    points = []

    for chunk in chunks:

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        deterministic_id = str(
            uuid.uuid5(
                uuid.NAMESPACE_DNS,
                chunk
            )
        )

        enriched_metadata = {
            **metadata,
            "memory_type": classify_memory_type(chunk),
            "priority": extract_priority(chunk),
            "tags": extract_tags(chunk)
        }

        points.append(
            PointStruct(
                id=deterministic_id,
                vector=embedding,
                payload={
                    "content": chunk,
                    "metadata": enriched_metadata
                }
            )
        )

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return {
        "chunks_stored": len(points)
    }