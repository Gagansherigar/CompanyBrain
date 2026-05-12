from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import os

from services.crm_service import (
    ingest_crm_data
)

from services.ingestion_service import (
    ingest_meeting_file
)

from services.slack_service import (
    ingest_slack_file
)

from services.support_service import (
    ingest_support_tickets
)

from fastapi import Body

from mcp.slack_mcp import (
    SlackMCPTool
)

from services.memory_ingestion_service import (
    ingest_memory_objects
)
router = APIRouter()

UPLOAD_DIRECTORY = (
    "uploaded_files"
)

os.makedirs(
    UPLOAD_DIRECTORY,
    exist_ok=True
)


@router.post("/ingest/meeting")
async def ingest_meeting(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    result = ingest_meeting_file(
        file_path
    )

    return result


@router.post("/ingest/slack")
async def ingest_slack(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    result = ingest_slack_file(
        file_path
    )

    return result

@router.post("/ingest/slack/live")
async def ingest_live_slack(
    data: dict = Body(...)
):

    tool = SlackMCPTool()

    memories = tool.fetch_messages(
        channel_id=data["channel_id"]
    )

    result = ingest_memory_objects(
        memories
    )

    return result

@router.post("/ingest/support")
async def ingest_support(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    result = ingest_support_tickets(
        file_path
    )

    return result

@router.post("/ingest/crm")
async def ingest_crm(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    result = ingest_crm_data(
        file_path
    )

    return result