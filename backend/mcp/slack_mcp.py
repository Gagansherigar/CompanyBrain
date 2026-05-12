from slack_sdk import WebClient
from dotenv import load_dotenv

import os

load_dotenv()


class SlackMCPTool:

    def __init__(self):

        self.client = WebClient(
            token=os.getenv(
                "SLACK_BOT_TOKEN"
            )
        )

    def fetch_messages(
        self,
        channel_id,
        limit=20
    ):

        response = (
            self.client.conversations_history(
                channel=channel_id,
                limit=limit
            )
        )

        memories = []

        for message in response["messages"]:

            memories.append({
                "source": "slack",
                "memory_type": "chat_message",
                "author": message.get(
                    "user",
                    ""
                ),
                "content": message.get(
                    "text",
                    ""
                ),
                "timestamp": message.get(
                    "ts",
                    ""
                ),
                "metadata": {
                    "channel_id": channel_id
                }
            })

        return memories