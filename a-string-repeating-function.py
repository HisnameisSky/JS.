def repeat_string_num_times(str_val,num):
    if num <= 0:
        return ""
    result = ""
    for _ in range(num):
        result += str_val
    return result

#variant

def repeat_string_num_times_smart(str_val,num):
    return str_val * num if num > 0 else ""