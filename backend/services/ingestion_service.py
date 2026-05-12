from connectors.meetings_connector import (
    MeetingsConnector
)

from ingestion.ingestion_pipeline import (
    process_document
)

from reasoning.decision_extractor import (
    extract_decisions
)


def ingest_meeting_file(file_path):

    connector = MeetingsConnector()

    text = connector.load_data(
        file_path
    )

    process_document(
        text,
        metadata={
            "source": "meeting"
        }
    )

    decisions = extract_decisions(
        text
    )

    return {
        "status": "success",
        "decisions": decisions
    }


def ingest_slack_file(file_path):

    return {
        "status": "not_implemented"
    }


def ingest_support_file(file_path):

    return {
        "status": "not_implemented"
    }


def ingest_crm_file(file_path):

    return {
        "status": "not_implemented"
    }