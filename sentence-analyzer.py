def get_vowel_count(sentence):
    vowels = "aeiou"
    count = 0

    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count


vowel_count = get_vowel_count("Apples are tasty fruits")
print(f"Vowel Count: {vowel_count}")


def get_consonant_count(sentence):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0

    for char in sentence.lower():
        if char in consonants:
            count += 1
    return count


consonant_count = get_consonant_count("Coding is fun")
print(f"Consonant Count: {consonant_count}")


def get_punctuation_count(sentence):
    punctuations = ".,!?;:-()[]{}\"'–"
    count = 0

    for char in sentence:
        if char in punctuations:
            count += 1
    return count


punctuation_count = get_punctuation_count("WHAT?!?!?!?!?")
print(f"Punctuation Count: {punctuation_count}")


def get_word_count(sentence):
    if sentence.strip() == "":
        return 0

    words = sentence.strip().split(" ")
    count = 0

    for word in words:
        if word != "":
            count += 1

    return count


word_count = get_word_count("I love freeCodeCamp")
print(f"Word Count: {word_count}")