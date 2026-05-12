from llm.gemini_client import (
    model
)

response = model.generate_content(
    "Explain vector embeddings."
)

print(response.text)