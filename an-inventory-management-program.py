inventory = []


def find_product_index(product_name):
    name_lower = product_name.lower()
    for i, item in enumerate(inventory):
        if item["name"].lower() == name_lower:
            return i
    return -1


def add_product(product):
    name_lower = product["name"].lower()
    index = find_product_index(name_lower)

    if index != -1:
        inventory[index]["quantity"] += product["quantity"]
        print(f"{name_lower} quantity updated")
    else:
        inventory.append({"name": name_lower, "quantity": product["quantity"]})
        print(f"{name_lower} added to inventory")


def remove_product(product_name, quantity):
    name_lower = product_name.lower()
    index = find_product_index(name_lower)

    if index == -1:
        print(f"{name_lower} not found")
        return

    current_quantity = inventory[index]["quantity"]

    if quantity > current_quantity:
        print(f"Not enough {name_lower} available, remaining pieces: {current_quantity}")
    else:
        inventory[index]["quantity"] -= quantity
        remaining_quantity = inventory[index]["quantity"]

        if remaining_quantity == 0:
            inventory.pop(index)

        print(f"Remaining {name_lower} pieces: {remaining_quantity}")