def find_longest_word_length(str_val):
    words = str_val.split(" ")
    max_length = 0

    for word in words:
        if len(word)> max_length:
            max_length = len(word)
    return max_length

#Long story short..
def find_longest_word_length_smart(str_val):
    return max(len(word) for word in str_val.slit(" "))

