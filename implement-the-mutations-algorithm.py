def mutation(arr):
    target = arr[0].lower()
    test = arr[1].lower()

    for char in test :
        if char not in target:
            return False
    return True

#Variant..
def mutation_smart(arr):
    return all(char in arr[0].lower() for char in arr[1].lower())

print(mutation(["alien","L1NE"]))