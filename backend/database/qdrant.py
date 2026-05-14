from qdrant_client import QdrantClient

from qdrant_client.models import (
    VectorParams,
    Distance,
    PayloadSchemaType
)
from dotenv import load_dotenv

load_dotenv()

import os


qdrant = QdrantClient(
    url=os.getenv(
        "QDRANT_URL"
    ),

    api_key=os.getenv(
        "QDRANT_API_KEY"
    )
)


COLLECTION_NAME = (
    "organizational_memory"
)


def create_collection():

    collections = qdrant.get_collections()

    existing_collections = [
        collection.name
        for collection in collections.collections
    ]

    if COLLECTION_NAME not in existing_collections:

        qdrant.create_collection(
            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        qdrant.create_payload_index(
            collection_name=COLLECTION_NAME,

            field_name="metadata.source",

            field_schema=PayloadSchemaType.KEYWORD
        )

        qdrant.create_payload_index(
            collection_name=COLLECTION_NAME,

            field_name="metadata.memory_type",

            field_schema=PayloadSchemaType.KEYWORD
        )

        qdrant.create_payload_index(
            collection_name=COLLECTION_NAME,

            field_name="metadata.priority",

            field_schema=PayloadSchemaType.KEYWORD
        )


def reset_collection():

    collections = qdrant.get_collections()

    existing_collections = [
        collection.name
        for collection in collections.collections
    ]

    if COLLECTION_NAME in existing_collections:

        qdrant.delete_collection(
            collection_name=COLLECTION_NAME
        )

    create_collection()


create_collection()