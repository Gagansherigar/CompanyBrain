from llm.embeddings import (
    create_embedding
)

from memory.memory_store import (
    store_memory
)

text = (
    "Engineering discussed ECS migration."
)

embedding = create_embedding(
    text
)

payload = {
    "content": text,
    "metadata": {
        "source": "meeting"
    }
}

store_memory(
    embedding,
    payload
)

print("Memory stored successfully")