def print_characters(string_val):
    for char in string_val:
        print(char)


print_characters("hello")


def get_matched_word_count(sentence, match):
    count = 0

    for word in sentence:
        if word == match:
            count += 1
        print(
            f'Checking "{word}" against "{match}" | Running count: {count}'
        )

    return count


print(
    get_matched_word_count(
        ["I", "really", "really", "really", "like", "to", "code"], "really"
    )
)

print(
    get_matched_word_count(
        ["Do", "not", "fear", "the", "dandy", "lion"], "dandy"
    )
)

##

def matched_word_count(sentence, match):
    return sentence.count(match)

print(
    get_matched_word_count(
        ["I", "really", "really", "really", "like", "to", "code"], "really"    
    )
)