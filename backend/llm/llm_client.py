import os

from dotenv import load_dotenv

from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def generate_text(
    prompt
):

    completion = (
        client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    )

    return (
        completion
        .choices[0]
        .message
        .content
    )