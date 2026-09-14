def drop_elements(arr, func):
    for i, elem in enumerate(arr):
        if func(elem):
            return arr[i:]
    return []