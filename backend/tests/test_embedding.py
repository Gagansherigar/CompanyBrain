from llm.embeddings import (
    create_embedding
)

text = (
    "Kubernetes maintenance overhead increased."
)

embedding = create_embedding(
    text
)

print(len(embedding))

print(embedding[:10])