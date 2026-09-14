def get_index_to_ins(arr,num):
    arr.sort()
    index = -1

    for i, element in enumerate(arr):
        if element >= num:
            index = i
            break

    return len(arr) if index == -1 else index

#variant

import bisect

def get_index_toindes(arr,num):
    arr.sort()
    return bisect.bisect_left(arr,num)