contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"],
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"],
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"],
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"],
    },
]

def look_up_profile(name,prop):
    for contact in contacts:
        if contact["firstName"] == name:
            if prop in contacts:
                return contact[prop]
            else: 
                return "No such property"
    return "No such contact"

#variant

def look_up_profile(name, prop):
    person= next(
        (c for c in contacts if c["firstName"] == name), None)
    if not person:
        return "No such contact"
    if prop in person:
        return person[prop]
    else:

        return "No such property"