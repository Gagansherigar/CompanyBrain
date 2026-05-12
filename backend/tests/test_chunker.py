from ingestion.chunker import (
    chunk_text
)

text = (
    "This is a long organizational "
    "discussion about infrastructure "
    "migration and operational issues."
)

chunks = chunk_text(
    text,
    chunk_size=20
)

print(chunks)