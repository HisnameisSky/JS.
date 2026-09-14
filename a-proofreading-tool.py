def is_palindrome(word):
    if not word:
        return False
    cleaned = word.lower()
    return cleaned == cleaned[::-1]


def find_palindrome_breaks(words):
    if not words:
        return []
    return [i for i, w in enumerate(words) if not is_palindrome(w)]


def find_repeated_phrases(words, phrase_length):
    if not words or phrase_length >= len(words) or phrase_length <= 0:
        return []

    phrases = []
    max_start = len(words) - phrase_length

    for i in range(max_start + 1):
        phrase_str = " ".join(words[i : i + phrase_length]).lower()
        phrases.append(phrase_str)

    counts = {}
    for p in phrases:
        counts[p] = counts.get(p, 0) + 1

    repeated_indices = []
    for i, p in enumerate(phrases):
        if counts[p] > 1:
            repeated_indices.append(i)

    return repeated_indices


def analyze_texts(texts, phrase_length):
    if not texts:
        return []

    result = []
    for words in texts:
        result.append(
            {
                "repeatedPhrases": find_repeated_phrases(words, phrase_length),
                "palindromeBreaks": find_palindrome_breaks(words),
            }
        )
    return result

#variant



def is_plindrome_two_pointers(string_val):
    if not string_val:
        return False
    cleaned = string_val.lower()
    left = 0
    right = len(cleaned) -1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_plindrome_two_pointers("racecar"))
print(is_plindrome_two_pointers("hello"))