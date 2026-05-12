from database.qdrant import (
    qdrant,
    COLLECTION_NAME
)

from llm.embeddings import (
    embedding_model
)

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)


def vector_search(
    query,
    source_filter=None,
    limit=5
):

    query_vector = (
        embedding_model.encode(
            query
        ).tolist()
    )

    search_filter = None

    if source_filter:

        search_filter = Filter(
            must=[
                FieldCondition(
                    key="metadata.source",
                    match=MatchValue(
                        value=source_filter
                    )
                )
            ]
        )

    response = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
        query_filter=search_filter
    )

    return response.points