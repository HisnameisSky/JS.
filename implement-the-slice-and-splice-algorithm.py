def franken_splice(arr1, arr2, n ):
    local_array = arr2.copy()
    local_array[n:n] = arr1
    return local_array