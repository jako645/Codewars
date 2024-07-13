def cakes(recipe, available) -> int:
    return min(available.get(item, 0) // recipe[item] for item in recipe)
