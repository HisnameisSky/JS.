print("Hi there!")
bot_name = "teacherBot"
greeting=f"My name is {bot_name}."
print(greeting)

subject="JavaScript"
topic="strings"
sentence=f"Today, you'll learn about {topic} in {subject}."
print(sentence)

str_length_intro=f"Here's an example of using the length proterty on the word {subject}"
print(str_length_intro)
print(len(subject))

print(f"Here is an example of using the length property on the word {topic}.")
print(len(topic))

print(f"Here is an example of accessing the first letter in the word {subject}.")
print(subject[0])

print(f"Here is an example of accessing the second letter in the word {subject}.")
print(subject[1])

last_character = subject[-1]
print(last_character)

learning_is_fun_sentence = "Learning is fun."
print("Here are examples of finding the positions of substrings in the sentence.")

print(learning_is_fun_sentence.find("fun"))
print(learning_is_fun_sentence.find("learning"))

print("I hope you enjoyed learning today.")