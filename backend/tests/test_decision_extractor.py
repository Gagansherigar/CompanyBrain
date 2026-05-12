from reasoning.decision_extractor import (
    extract_decisions
)

meeting_text = """
Engineering leadership discussed
migrating from Kubernetes to ECS
because deployment outages increased.
"""

result = extract_decisions(
    meeting_text
)

print(result)