from pydantic import BaseModel
from typing import List


class DecisionModel(BaseModel):

    decision: str
    reasoning: List[str]
    risks: List[str]
    action_items: List[str]