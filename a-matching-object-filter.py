def what_is_in_a_name(collection, source):
    return [
        obj
        for obj in collection
        if all(key in obj and obj[key] == source[key] for key in source.keys())
    ]

#

def what_is_in_name_pythonic(collection, source):
    source_items = source.items()
    return [obj for obj in collection if source_items <= obj.items()]