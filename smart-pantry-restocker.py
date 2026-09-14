import json

pantry = [
    {
        "sku": "A10",
        "name": "Tomatoes",
        "qty": 4,
        "expires": "2027-01-01",
        "zone": "fridge",
    },
    {
        "sku": "D43",
        "name": "Pineapples",
        "qty": 2,
        "expires": "2020-01-01",
        "zone": "general",
    },
]

raw_data = [
    "A10|Tomatoes|5|2027-01-01",
    "B21|Bananas|10|2027-01-01",
    "C32|Eggs|3|2027-01-01|fridge",
    "C32|Eggs|3|2027-01-01",
    "D43|Pineapples|0|2027-01-01",
    "E54|Peppers|-1|2027-01-01|fridge",
]

def parse_shipment (raw_data) :
    result = []
    seen_skus = set()

    for item_str in raw_data:
        parts = item_str.split("|")
        sku = parts[0]
        name = parts[1]
        qty = int(parts[2])
        expires = parts[3]

        zone = parts[4] if len(parts) > 4 else "genetal"

        if sku not in seen_skus:
            seen_skus.add(sku)
            result.append(
                {
                    "sku": sku,
                    "name": name,
                    "qty": qty,
                    "expires": expires,
                    "zone": zone,
                }
            )
    return result

def plan_restock(pantry, shipment):
    actions = []
    pantry_skus = [item["sku"] for item in pantry]

    for item in shipment:
        if item["qty"] <=0:
            action_type = "discard"
        elif item["sku"] in pantry_skus:
            action_type = "restock"
        else:
            action_type = "donate"
        actions.append({"type": action_type, "item": item})
    return actions

def group_by_zone(actions):
    grouped = {}
    for action in actions :
        zone = action ["item"]["zone"]
        if zone not in grouped:
            grouped[zone] = []
        grouped[zone].append(action)
    return grouped

def clone_pantry(pantry):
    return json.loads(json.dumps(pantry))

parsed_shipment = parse_shipment(raw_data)
restock_plan = plan_restock(pantry, parsed_shipment)
grouped_results = group_by_zone(restock_plan)

print(grouped_results)