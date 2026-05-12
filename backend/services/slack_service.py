from connectors.slack_connector import (
    SlackConnector
)

from ingestion.ingestion_pipeline import (
    process_document
)


def ingest_slack_file(
    file_path
):

    connector = SlackConnector()

    messages = connector.load_data(
        file_path
    )

    combined_text = ""

    for message in messages:

        combined_text += (
            f"""
            User: {message.get('user', '')}
            Channel: {message.get('channel', 'general')}
            Message: {message.get('text', '')}
            Timestamp: {message.get('timestamp', '')}
            """
        )

    process_document(
        combined_text,
        metadata={
            "source": "slack"
        }
    )

    return {
        "status": "success",
        "messages_ingested": len(messages)
    }