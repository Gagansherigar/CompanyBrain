from services.ingestion_service import (
    ingest_meeting_file
)

result = ingest_meeting_file(
    "sample_data/meetings/meeting1.txt"
)

print(result)