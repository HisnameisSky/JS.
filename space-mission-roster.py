squad = []

first_astronaut = {
    "id": 1,
    "name": "Andy",
    "role": "Commander",
    "isEVAEligible": True,
    "priority": 3,
}

def add_crew_member(crew, astronaut):
    for member in crew:
        if member["id"] == astronaut["id"]:
            print("Duplicate ID: " + str(astronaut["id"]))
            return
    crew.append(astronaut)

add_crew_member(squad, first_astronaut)

remaining_crew = [
    {
        "id": 2,
        "name": "Bart",
        "role": "Pilot",
        "isEVAEligible": False,
        "priority": 8,
    },
    {
        "id": 3,
        "name": "Caroline",
        "role": "Engineer",
        "isEVAEligible": True,
        "priority": 4,
    },
    {
        "id": 4,
        "name": "Diego",
        "role": "Scientist",
        "isEVAEligible": False,
        "priority": 1,
    },
    {
        "id": 5,
        "name": "Elise",
        "role": "Medic",
        "isEVAEligible": True,
        "priority": 7,
    },
    {
        "id": 6,
        "name": "Felix",
        "role": "Navigator",
        "isEVAEligible": True,
        "priority": 6,
    },
    {
        "id": 7,
        "name": "Gertrude",
        "role": "Communications",
        "isEVAEligible": False,
        "priority": 4,
    },
    {
        "id": 8,
        "name": "Hank",
        "role": "Mechanic",
        "isEVAEligible": True,
        "priority": 2,
    },
    {
        "id": 9,
        "name": "Irene",
        "role": "Specialist",
        "isEVAEligible": True,
        "priority": 5,
    },
    {
        "id": 10,
        "name": "Joan",
        "role": "Technician",
        "isEVAEligible": False,
        "priority": 1,
    },
]

for member in remaining_crew:
    add_crew_member(squad,member)

def swap_crew_members(crew, from_index, to_index):
    if (
        from_index < 0
        or to_index < 0
        or from_index >= len(crew)
        or to_index >= len(crew)
    ):
        print("Invalid crew indices")
        return

    updated_crew = crew.copy()
    updated_crew[from_index], updated_crew[to_index] = (
        updated_crew[to_index],
        updated_crew[from_index],
    )

    return updated_crew

updated_squad = swap_crew_members(squad, 2,5)

def sort_by_priority_descending(crew):
    n=len(crew)
    for i in range(n-1):
        for j in range(n-1-i):
            if crew[j]["priority"]<crew[j+1]["priority"]:
                crew[j],crew[j+1],crew[j+1],crew[j]

def get_eva_ready_crew(crew):
    eligible = []
    for astronaut in crew:
        if astronaut["isEVAEligible"]:
            eligible.append(astronaut)
    sort_by_priority_descending(eligible)
    return eligible

get_eva_ready_squad = get_eva_ready_crew(updated_squad)

def chunk_crew(crew,size):
    if size < 1:
        print("Chunk size must be >= 1")
        return
    chunks = []
    for i in range(0,len(crew),size):
        chunks.append(crew[i:i+size])
    return chunks

eva_chunks = chunk_crew(get_eva_ready_squad, 3)

def print_crew_summary(crew):
    sorted_crew = crew.copy()
    sort_by_priority_descending(sorted_crew)
    for astronaut in sorted_crew:
        print(astronaut["name"])

print_crew_summary(updated_squad)