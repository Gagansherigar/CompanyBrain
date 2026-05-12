import json

from connectors.base_connector import (
    BaseConnector
)


class SupportConnector(BaseConnector):

    def load_data(
        self,
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)