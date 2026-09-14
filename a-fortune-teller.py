import random
import math

fortune1 = "Your cat will look very cuddly today."
fortune2 = "The weather will be nice tomorrow."
fortune3 = "Be cautious of your new neighbors."
fortune4 = "You will find a new hobby soon."
fortune5 = "It would be wise to avoid the color red today."

random_number = math.floor(random.random() * 5) + 1

selected_fortune = None

if random_number == 1:
    selected_fortune = fortune1
elif random_number == 2:
    selected_fortune = fortune2
elif random_number == 3:
    selected_fortune = fortune3
elif random_number == 4:
    selected_fortune = fortune4
elif random_number == 5:
    selected_fortune = fortune5

print(selected_fortune)