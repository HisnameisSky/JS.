tiger = {"species": "Tiger", "age": 5, "is_endangered": True}

elephant = {"species": "Elephant", "age": 10, "is_endangered": True}

def get_property(animal, property_name):
    return animal[property_name]


print(get_property(tiger, "species"))  # "Tiger"
print(get_property(elephant, "age"))  # 10