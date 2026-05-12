def analyze_root_cause(events):

    causes = []

    for event in events:

        content = event.payload.get(
            "content",
            ""
        )

        if "outage" in content.lower():

            causes.append(content)

    return {
        "possible_root_causes": causes
    }