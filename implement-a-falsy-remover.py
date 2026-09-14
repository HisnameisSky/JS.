def bouncer(arr):
    return [item for item in arr if bool(item)]

def bouncer_filter(arr):
    return list(filter(None, arr))