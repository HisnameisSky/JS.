from dataclasses import dataclass

@dataclass(frozen=True)
class Plant:
    common_name:str
    scientific_name:str
    cultivar:str

ballerina = Plant("Spanish lavender", "Lavandula stoechas", "Ballerina")
pretty_polly = Plant("Spanish lavender", "Lavandula stoechas", "Pretty Polly")
willow_vale = Plant("Spanish lavender", "Lavandula stoechas", "Willow Vale")
hidcote = Plant("English lavender", "Lavandula angustifolia", "Hidcote")
imperial_gem = Plant("English lavender", "Lavandula angustifolia", "Imperial Gem")
royal_crown = Plant("French lavender", "Lavandula dentata", "Royal Crown")

catalog = {
    ballerina: {"small": 20, "medium": 15, "large": 12},
    pretty_polly: {"small": 31, "medium": 14, "large": 24},
    willow_vale: {"small": 3, "medium": 5, "large": 0},
    hidcote: {"small": 33, "medium": 13, "large": 18},
    imperial_gem: {"small": 19, "medium": 35, "large": 28},
    royal_crown: {"small": 40, "medium": 22, "large": 9},
}

def sell_plants(plant: Plant, size: str, pots_no: int) -> str:
    if plant not in catalog:
        return "Item not found."
    
    name = f"{plant.scientific_name} '{plant.cultivar}'"
    pots = catalog[plant]
    
    if pots[size] - pots_no < 0:
        return f"Not enough {size} size pots for {name}. Only {pots[size]} left."
    
    pots[size] -= pots_no
    return "Catalog successfully updated."

def remove_plant(plant:Plant):
    return catalog.pop(plant, None)

def display_catalog() -> str:
    catalog_string = ""
    for key, val in catalog.items():
        catalog_string += f"{key.scientific_name} '{key.cultivar}': {val['small']} S, {val['medium']} M, {val['large']} L\n"
    return catalog_string

def display_plants_set() -> set:
    common_names = []
    for key in catalog.keys():
        common_names.append(key.common_name)
    
    return set(common_names)

plants_set = display = display_plants_set()
print(plants_set)