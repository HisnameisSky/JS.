import copy 

def compact_fragments(fragments):
    result = [f for f in fragments if f is not None]
    if len(result) < len(fragments):
        print("[COMPACTED] Removed None elements.")
    return result
def sort_fragments(fragments):
    result = copy.deepcopy(fragments)
    n = len(result)
    for i in range(n-1):
        for j in range(n-1-i):
            if result[j]["id"]> result[j+1]["id"]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def dedupe_fragments(fragments):
    result = []
    seen_ids = set()
    for item in fragments:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            result.append(item)
        else:
            print(f"[DEDUPED] Duplicate id found: {item['id']}")
    return result

def fill_missing_fragments(fragments):
    if not fragments:
        return []
    result = []
    for i ,current in enumerate(fragments):
        if i > 0:
            prev_id = result [-1]["id"]
            for missing_id in range(prev_id +1, current ["id"]):
                result.append({"id": missing_id, "text": "[...]"})
                print(f"[FILLED] Added placeholder for missing id: {missing_id}")    
        result.append(current)
    return result