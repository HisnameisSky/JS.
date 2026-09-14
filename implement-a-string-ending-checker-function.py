def confirm_ending(str_val,target):
    target_length = len(target)
    ending = str_val[-target_length:]
    return ending == target

