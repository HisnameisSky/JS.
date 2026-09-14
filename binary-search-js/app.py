import math

def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1

    while low <= high:
        # Pythonの整除演算子 // で Math.floor((low + high) / 2) を再現
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return [path_to_target, f"Value found at index {mid}"]
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [[], "Value not found"]


# === 動作確認 ===
if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 3))
    # 返り値: [[3], 'Value found at index 2']

    print(binary_search([1, 2, 3, 4, 5, 9], 4))
    # 返り値: [[3, 4], 'Value found at index 3']

    print(binary_search([1, 3, 5, 9, 14, 22], 10))
    # 返り値: [[], 'Value not found']


##bubble sort

def bubble_sort(arr):
    n=len(arr)
    arr=arr.copy()

    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubble_sort([5,3,1,4,2]))

##selection sort

def selection_sort(arr):
    n=len(arr)
    arr=arr.copy()

    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

print(selection_sort([5,3,1,2,4,2]))