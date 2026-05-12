import uuid

from qdrant_client.models import PointStruct

from database.qdrant import (
    qdrant,
    COLLECTION_NAME
)


def store_memory(
    embedding,
    payload
):

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload=payload
            )
        ]
    )