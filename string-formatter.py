user_input = "   Hello World!   "
print("Original input:")
print(user_input)

cleaned_input = user_input.strip()
print("Result of trimming whitespace from both ends:")
print(cleaned_input)

trimmed_start = user_input.lstrip()
print("After using the trimStart() method, leading spaces removed:")
print(trimmed_start)

trimmed_end = user_input.rstrip()
print("After using the trimEnd() method, trailing spaces removed:")
print(trimmed_end)

upper_case_input = cleaned_input.upper()
print("Result of using the toUpperCase() method:")
print(upper_case_input)

lower_case_input = cleaned_input.lower()
print("Result of using the toLowerCase() method:")
print(lower_case_input)

lowercase_word = "camelcase"
camel_cased_version = lowercase_word[:5] + lowercase_word[5].upper() + lowercase_word[-3:]
print("Camel cased version:")
print(camel_cased_version)