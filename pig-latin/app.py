import re

def translate_pig_latin(s:str) -> str:
    vowel_pattern = r"[aeiou]"
    if re.match(vowel_pattern,s[0]):
        return s + "way"
    match = re.search(vowel_pattern, s)
    if not match:
        return s + "ay"

    first_vowel_idx = match.start()
    consonants = s[:first_vowel_idx]
    rest=s[first_vowel_idx:]
    return rest + consonants + "ay"

print(translate_pig_latin("california"))  # -> aliforniacay
print(translate_pig_latin("glove"))  # -> oveglay
print(translate_pig_latin("algorithm"))  # -> algorithmway
print(translate_pig_latin("schwartz"))  # -> artzschway
print(translate_pig_latin("rhythm"))  # -> rhythmay