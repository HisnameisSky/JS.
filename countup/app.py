def countup(number:int)->list[int]:
    if number < 1:
        return []
    else:
        count_array = countup(number -1)
        count_array.append(number)
        return count_array
print(countup(5))