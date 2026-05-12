import json

from connectors.base_connector import (
    BaseConnector
)


class SlackConnector(BaseConnector):

    def load_data(
        self,
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        messages = []

        for item in data:

            messages.append({
                "user": item.get("user"),
                "text": item.get("text"),
                "timestamp": item.get("ts")
            })

        return messages