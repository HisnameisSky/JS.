import math

def largest_of_all(arr):
    results = []
    for sub_arr in arr:
        max_num = sub_arr[0]
        for num in sub_arr[1:]:
            if num > max_num:
                max_num = num
            results.append(max_num)
    return results

#variant

def largest_of_all_pythonic(arr):
    return [max(sub_arr) for sub_arr in arr]

#ex

sub_arr = [13,27,18]

print(max(*sub_arr))

#ex2

fruits = ["🍎", "🍌"]
vegetables = ["🥦", "🥕"]

food_list = [*fruits, *vegetables]

original = [1,2,3]
copy_arr = [*original]

print(copy_arr)