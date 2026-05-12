from database.qdrant import (
    qdrant,
    COLLECTION_NAME
)

collections = qdrant.get_collections()

print(collections)

print(
    f"Connected to collection: {COLLECTION_NAME}"
)