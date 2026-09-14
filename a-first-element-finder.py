def find_element(arr, func) :
    for item in arr:
        if func(item):
            return item
    return None

def find_element_pythonic(arr, func) :
    return next((item for item in arr if func(item)), None)

#callback ex

def find_element1(arr, func) :
    for item in arr:
        if func(item):
            return item
    return None

def is_even(num):
    return num % 2 ==0

print(find_element1([1,3,8], is_even))