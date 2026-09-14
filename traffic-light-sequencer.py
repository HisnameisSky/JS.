config1 = {
    "fault": False,
    "phases": [
        {"color": "green", "duration": 5},
        {"color": "yellow", "duration": 2},
        {"color": "red", "duration": 4},
    ],
}

config2 = {
    "fault": False,
    "phases": [
        {"color": "red", "duration": 3},
        {"color": "yellow", "duration": -2},
        {"color": "green", "duration": 6},
    ],
}

config3 = {
    "fault": True,
    "phases": [
        {"color": "green", "duration": 5},
        {"color": "yellow", "duration": 2},
        {"color": "red", "duration": 6},
    ],
}

config4 = {"fault": False, "phases": []}

def run_sequence(config, cycles):
    if not config.get("phases") or len(config["phases"]) == 0:
        print("No phases found")
        return

    for _ in range(cycles):
        if config.get("fault"):
            print("Faulted phase!")
            return

        for phase in config["phases"]:
            if phase["duration"] <= 0:
                print("Invalid phase detected")
            else:
                print(
                    f"Switching to {phase['color']} for {phase['duration']} s"
                )


def generate_timeline(config, cycles):
    timeline = []
    total_time = 0

    if not config.get("phases") or len(config["phases"]) == 0:
        return timeline

    for _ in range(cycles):
        for phase in config["phases"]:
            total_time += phase["duration"]
            timeline.append(total_time)

    return timeline