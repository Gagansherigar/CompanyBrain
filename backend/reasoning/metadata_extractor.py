def extract_tags(text):

    tags = []

    lowered = text.lower()

    keyword_map = {
        "deployment": [
            "deployment",
            "deploy"
        ],
        "kubernetes": [
            "kubernetes",
            "k8s"
        ],
        "incident": [
            "incident",
            "outage",
            "failure"
        ],
        "ecs": [
            "ecs"
        ],
        "latency": [
            "latency",
            "slow"
        ]
    }

    for tag, keywords in keyword_map.items():

        for keyword in keywords:

            if keyword in lowered:

                tags.append(tag)

                break

    return list(set(tags))


def classify_memory_type(text):

    lowered = text.lower()

    if (
        "outage" in lowered
        or "incident" in lowered
        or "failure" in lowered
    ):

        return "incident"

    if (
        "migrate" in lowered
        or "proposal" in lowered
        or "decision" in lowered
    ):

        return "decision"

    if (
        "customer" in lowered
        or "support" in lowered
        or "complaint" in lowered
    ):

        return "customer_issue"

    return "general"


def extract_priority(text):

    lowered = text.lower()

    if (
        "critical" in lowered
        or "urgent" in lowered
        or "high" in lowered
    ):

        return "high"

    if "medium" in lowered:

        return "medium"

    return "low"