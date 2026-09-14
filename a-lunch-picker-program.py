import math
import random

lunches = []


def add_lunch_to_end(array, item):
    array.append(item)
    print(f"{item} added to the end of the lunch menu.")
    return array


def add_lunch_to_start(array, item):
    array.insert(0, item)
    print(f"{item} added to the start of the lunch menu.")
    return array


def remove_last_lunch(array):
    if len(array) == 0:
        print("No lunches to remove.")
    else:
        removed_item = array.pop()
        print(f"{removed_item} removed from the end of the lunch menu.")
    return array


def remove_first_lunch(array):
    if len(array) == 0:
        print("No lunches to remove.")
    else:
        removed_item = array.pop(0)
        print(f"{removed_item} removed from the start of the lunch menu.")
    return array


def get_random_lunch(array):
    if len(array) == 0:
        print("No lunches available.")
    else:
        selected_item = random.choice(array)
        print(f"Randomly selected lunch: {selected_item}")


def show_lunch_menu(array):
    if len(array) == 0:
        print("The menu is empty.")
    else:
        print(f"Menu items: {', '.join(array)}")