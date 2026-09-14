record_collection = {
    2548: {
        "albumTitle": "Slippery When Wet",
        "artist": "Bon Jovi",
        "tracks": ["Let It Rock", "You Give Love a Bad Name"],
    },
    2468: {
        "albumTitle": "1999",
        "artist": "Prince",
        "tracks": ["1999", "Little Red Corvette"],
    },
    1245: {"artist": "Robert Palmer", "tracks": []},
    5439: {"albumTitle": "ABBA Gold"},
}

def update_records(records, record_id, prop, value):
    if value == "":
        if prop in records[record_id]:
            del records[record_id][prop]

    elif prop != "tracks":
        records[record_id][prop] = value

    else:
        if "tracks" not in records[record_id]:
            records[record_id]["tracks"] = []

        records[record_id]["tracks"].append(value)

    return records
update_records(record_collection, 5439, "artist", "ABBA")
update_records(record_collection, 5439, "tracks", "Take a Chance on Me")
print(record_collection[5439])