"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from dish_ingredients."""
    
    ingredient_set = set(dish_ingredients)
    return (dish_name, ingredient_set)


def check_drinks(drink_name, drink_ingredients):
    """Append Cocktail or Mocktail based on alcohol presence."""
    
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredients."""
    
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Return ingredients that are special/allergens."""
    
    dish_name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS
    
    return (dish_name, special)


def compile_ingredients(dishes):
    """Compile master ingredient list."""
    
    master = set()

    for dish in dishes:
        master |= dish

    return master


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from main dish list."""
    
    dish_set = set(dishes)
    appetizer_set = set(appetizers)

    return list(dish_set - appetizer_set)


def singleton_ingredients(dishes, intersection):
    """Find ingredients appearing only once across dishes."""
    
    all_ingredients = set()

    for dish in dishes:
        all_ingredients |= dish

    singleton = all_ingredients - intersection

    return singleton