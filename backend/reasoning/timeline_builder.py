def build_timeline(events):

    sorted_events = sorted(
        events,
        key=lambda x: x.get(
            "timestamp",
            ""
        )
    )

    return sorted_events