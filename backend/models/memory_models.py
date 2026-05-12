from pydantic import BaseModel
from typing import Dict


class MemoryModel(BaseModel):

    content: str
    metadata: Dict