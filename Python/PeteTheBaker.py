def cakes(recipe, available) -> int:
    number_of_cakes_pro_item = []
    for item_name in recipe:
        try:
            number_of_cakes_pro_item.append(
                available[item_name] // recipe[item_name])
        except KeyError:
            # Raised when item from recipe is not available
            return 0

    return min(number_of_cakes_pro_item)

if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}

    print(cakes(recipe, available))
