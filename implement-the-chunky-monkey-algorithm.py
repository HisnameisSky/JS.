def chink_array_in_groups(arr,size):
    result = []
    for i in range(0, len(arr), size):
        result.append(arr[i:i+size])
    return result

#variant

def chink_array_in_groups_smart(arr,size):
    return [arr[i:i+size] for i in range(0, len(arr), size)]

#variant

def chunk_array_in_groups_while(arr,size):
    result = []
    arr_copy = arr.copy()
    while len(arr_copy) > 0:
        result.sppend(arr_copy[:size])
        arr_copy[:size] = []
        
    return result