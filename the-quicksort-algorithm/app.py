def quicksort(array:list)->list:
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = [x for x in array[:-1] if x < pivot]
    right = [x for x in array[:-1] if x >= pivot]

    return quicksort(left)+[pivot]+quicksort(right)

if __name__ == "__main__":
    test_data = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
    sorted_data = quicksort(test_data)
    print("ソート結果:", sorted_data)