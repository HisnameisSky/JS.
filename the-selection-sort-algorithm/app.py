def selection_sort(array:list)->list:
    arr=array.copy()
    n=len(arr)

    for i in range(n-1):
        min_index=1

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        if min_index != i:

            arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

if __name__ == "__main__":
    test_data = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
    sorted_data = selection_sort(test_data)
    print("ソート結果:",sorted_data)