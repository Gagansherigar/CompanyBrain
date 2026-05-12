from ingestion.cleaner import (
    clean_text
)

dirty_text = """
Hello


This     text
has messy spacing.
"""

cleaned = clean_text(
    dirty_text
)

print(cleaned)