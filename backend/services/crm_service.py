from connectors.crm_connector import (
    CRMConnector
)

from ingestion.ingestion_pipeline import (
    process_document
)


def ingest_crm_data(
    file_path
):

    connector = CRMConnector()

    records = connector.load_data(
        file_path
    )

    combined_text = ""

    for record in records:

        combined_text += (
            f"""
            Customer: {record['customer']}
            Deal Stage: {record['deal_stage']}
            Issue: {record['issue']}
            Priority: {record['priority']}
            """
        )

    process_document(
        combined_text,
        metadata={
            "source": "crm"
        }
    )

    return {
        "status": "success",
        "crm_records_ingested": len(records)
    }