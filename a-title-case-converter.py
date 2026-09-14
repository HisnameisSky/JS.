def title_case(str_val):
    return str_val.title()

#manual

def title_case_manual(str_val):
    words = str_val.lower().split(" ")
    return " ".join(word.capitalie() for word in words)