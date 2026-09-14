original_string = "I love cats."
print("Original string:")
print(original_string)

replaced_string = original_string.replace("cats", "dogs")
print("After using the replace() method:")
print(replaced_string)

example_sentence = "I love cats and cats are so much fun!"
print("Original sentence:")
print(example_sentence)

dogs_only_sentence = example_sentence.replace("cats", "dogs")
print("Replacing all occurrences of cats with dogs:")
print(dogs_only_sentence)

learning_sentence = "I love learning!"
print("Original learning sentence:")
print(learning_sentence)

repeated_love = ("love " * 3).rstrip()
print(repeated_love)

new_sentence = f"I {repeated_love} learning."
print(new_sentence)