print("Grocery shopping list")

shopping_list = []

print("It will be nice to have some fruit to eat.")

shopping_list.append("Apples")


def get_shopping_list_msg(arr):
    return f"Current Shopping List: {', '.join(arr)}"


print(get_shopping_list_msg(shopping_list))

shopping_list.append("Grapes")
print(get_shopping_list_msg(shopping_list))

print("It looks like we need to get some cooking oil.")

shopping_list.insert(0, "Vegetable Oil")
print(get_shopping_list_msg(shopping_list))

shopping_list.extend(["Popcorn", "Beef Jerky", "Potato Chips"])
print(get_shopping_list_msg(shopping_list))

print("This looks like too much junk food.")

shopping_list.pop()
print(get_shopping_list_msg(shopping_list))

print("It might be nice to get a dessert.")

shopping_list.insert(0, "Chocolate Cake")
print(get_shopping_list_msg(shopping_list))

print("On second thought, maybe we should be more health conscious.")

shopping_list.pop(0)
shopping_list[0] = "Canola Oil"

print(get_shopping_list_msg(shopping_list))