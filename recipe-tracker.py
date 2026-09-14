recipes =[]

recipe1 = {
    "name": "Spaghetti Carbonara",
    "ingredients": ["spaghetti", "Parmesan cheese", "pancetta", "black pepper"],
    "cookingTime": 22,
    "totalIngredients": None,
    "difficultyLevel": "",
}

recipe2 = {
    "name": "Chicken Curry",
    "ingredients": [
        "chicken breast",
        "coconut milk",
        "curry powder",
        "onion",
        "garlic",
    ],
    "cookingTime": 42,
    "totalIngredients": None,
    "difficultyLevel": "",
}

recipe3 = {
    "name": "Vegetable Stir Fry",
    "ingredients": ["broccoli", "carrot", "bell pepper"],
    "cookingTime": 15,
    "totalIngredients": None,
    "difficultyLevel": "",
}

recipes.extend([recipe1,recipe2,recipe3])

def get_total_ingredients(ingredients):
    return len(ingredients)


def get_difficulty_level(cooking_time):
    if cooking_time <= 30:
        return "easy"
    elif cooking_time <= 60:
        return "medium"
    else:
        return "hard"

recipe1_total_ingredients = get_total_ingredients(recipe1["ingredients"])
print(recipe1_total_ingredients)

recipe1_difficulty_level = get_difficulty_level(recipe1["cookingTime"])
print(recipe1_difficulty_level)

recipe1["totalIngredients"] = get_total_ingredients(recipe1["ingredients"])
recipe1["difficultyLevel"] = get_difficulty_level(recipe1["cookingTime"])

recipe2["totalIngredients"] = get_total_ingredients(recipe2["ingredients"])
recipe2["difficultyLevel"] = get_difficulty_level(recipe2["cookingTime"])

recipe3["totalIngredients"] = get_total_ingredients(recipe3["ingredients"])
recipe3["difficultyLevel"] = get_difficulty_level(recipe3["cookingTime"])

print(recipes)