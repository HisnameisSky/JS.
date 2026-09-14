def fear_not_letter(string_val):
    for i in range(len(string_val)-1):
        current_code = ord(string_val[i])
        next_code = ord(string_val[i + 1])

        if next_code != current_code +1 :
            return chr(current_code +1)
    return None

#variant

import string

def fear_not_letter1(string_val):
    alphabet = string.ascii_lowercase

    start_index = alphabet.index(string_val[0])

    for i in range(len(string_val)):
        if string_val[i] != alphabet[start_index + i]:
            return alphabet[start_index + i]
    return None
