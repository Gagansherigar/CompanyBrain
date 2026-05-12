from slack_sdk import WebClient
from dotenv import load_dotenv

import os

load_dotenv()


class SlackMCPClient:

    def __init__(self):

        self.client = WebClient(
            token=os.getenv(
                "SLACK_BOT_TOKEN"
            )
        )

    def get_channel_messages(
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

        normalized_messages = []

        for message in response["messages"]:

            normalized_messages.append({
                "source": "slack",
                "user": message.get(
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
                )
            })

        return normalized_messages