import math
import random

bot_name = "MathBot"
greeting = f"Hi there! My name is {bot_name} and I am here to teach you about the Math object!"

print(greeting)

print("The Math.random() method returns a pseudo random number greater than or equal to 0 and less than 1.")

random_num = random.random()
print(random_num)

print("Now, generate a random number between two values.")

min_val = 1
max_val = 100

random_num2 = random.random() * (max_val - min_val) + min_val
print(random_num2)

print("The Math.floor() method rounds the value down to the nearest whole integer.")

num_rounded_down = math.floor(6.7)
print(num_rounded_down)

print("Now, generate a random integer between two values.")

random_int = math.floor(random.random() * (max_val - min_val) + min_val)
print(random_int)

print("The Math.ceil() method rounds the value up to the nearest whole integer.")

num_rounded_up = math.ceil(3.2)
print(num_rounded_up)

print(
    "The Math.round() method rounds the value to the nearest whole integer."
)

num_rounded = round(2.7)
print(num_rounded)
num_rounded2 = round(11.2)
print(num_rounded2)

print("The Math.max() and Math.min() methods are used to get the maximum and minimum number from a range.")

max_num = max(3, 125, 55, 24)
print(max_num)
min_num = min(6, 90, 14, 90, 2)
print(min_num)

print("It was fun learning about the different Math methods with you!")