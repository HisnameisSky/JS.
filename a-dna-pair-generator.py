def pair_element(string):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}    
    return [[char, pairs[char]] for char in string]