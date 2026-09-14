morning_gates = [
    {"id": "North", "capacity": 5, "queue": [3, 6, 2, 4]},
    {"id": "East", "capacity": 3, "queue": [2, 4, 3, 5]},
    {"id": "South", "capacity": 4, "queue": [1, 2, 3, 1]},
    {"id": "West", "capacity": 2, "queue": [4, 1, 2, 3]},
]

night_gates = [
    {"id": "North", "capacity": 4, "queue": [6, 2, 5, 1]},
    {"id": "East", "capacity": 2, "queue": [3, 3, 4, 2]},
    {"id": "South", "capacity": 5, "queue": [2, 1, 2, 3]},
    {"id": "West", "capacity": 3, "queue": [5, 2, 1, 4]},
]


def initialize_throughput(gates):
    summary = {}
    for gate in gates:
        summary[gate["id"]] = 0
    return summary


def process_gate_flow(gate, tick_index):
    current_tick_queue = gate["queue"][tick_index]
    processed = 0
    while current_tick_queue > 0 and processed < gate["capacity"]:
        current_tick_queue -= 1
        processed += 1
    return {"processed": processed, "overflow": current_tick_queue}


def reroute_overflow(gates, current_gate, tick_index, overflow_amount):
    current_index = gates.index(current_gate)
    next_gate_index = (current_index + 1) % len(gates)
    gates[next_gate_index]["queue"][tick_index] += overflow_amount
    print(
        f"{overflow_amount} attendees rerouted to {gates[next_gate_index]['id']}"
    )


def handle_gate_at_tick(gates, gate, tick_index, throughput_summary):
    print(f"\nProcessing {gate['id']}...")
    print(f"{gate['queue'][tick_index]} attendees arriving.")
    result = process_gate_flow(gate, tick_index)
    throughput_summary[gate["id"]] += result["processed"]
    if result["overflow"] > 0:
        print(f"Overflow of {result['overflow']} attendees. Rerouting...")
        reroute_overflow(gates, gate, tick_index, result["overflow"])


def print_summary(summary):
    print("\nThroughput Summary")
    for gate_id, total_processed in summary.items():
        print(f"{gate_id}: {total_processed} attendees processed")


def simulate_festival(gates, time_block):
    print(f"\n{time_block} Simulation")
    throughput_summary = initialize_throughput(gates)
    max_ticks = len(gates[0]["queue"])
    tick_index = 0
    while tick_index < max_ticks:
        print(f"\nTick {tick_index + 1}")
        for gate in gates:
            handle_gate_at_tick(gates, gate, tick_index, throughput_summary)
        tick_index += 1
    print_summary(throughput_summary)


simulate_festival(morning_gates, "Morning")
simulate_festival(night_gates, "Night")