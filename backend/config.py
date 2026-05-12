import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

QDRANT_HOST = os.getenv(
    "QDRANT_HOST",
    "localhost"
)

QDRANT_PORT = int(
    os.getenv("QDRANT_PORT", 6333)
)