def unite_unique(*arrays):
    result = []
    seen = set()

    for arr in arrays:
        for item in arr:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result