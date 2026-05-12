from connectors.support_connector import (
    SupportConnector
)

from ingestion.ingestion_pipeline import (
    process_document
)


def ingest_support_tickets(
    file_path
):

    connector = SupportConnector()

    tickets = connector.load_data(
        file_path
    )

    combined_text = ""

    for ticket in tickets:

        combined_text += (
            f"""
            Ticket ID: {ticket['ticket_id']}
            Title: {ticket['title']}
            Description: {ticket['description']}
            Priority: {ticket['priority']}
            """
        )

    process_document(
        combined_text,
        metadata={
            "source": "support_ticket"
        }
    )

    return {
        "status": "success",
        "tickets_ingested": len(tickets)
    }