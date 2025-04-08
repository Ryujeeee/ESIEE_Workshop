#TASK : create a function to cook your favorite dish 
#favorite_dish:
#- parameters
#- methods - processes
#- conditions
def cook_spaghetti(ingredients):
    required_ingredients = {
        "pasta": {"types": "spaghetti", "amount": 200},
        "tomato sauce": {"amount": 100},
        "garlic": {"amount": 2},
        "olive oil": {"amount": 10}
    }
    
    for ingredient, details in required_ingredients.items():
        if ingredient not in ingredients:
            print(f"Missing {ingredient}! Can't cook spaghetti.")
            break
        elif ingredients[ingredient]["amount"] < details["amount"]:
            print(f"Not enough {ingredient}! Need at least {details['amount']}.")
            break
    else:
        print("All ingredients are present in sufficient amounts. Cooking spaghetti...")
        print("Cooking pasta...")
        print("Preparing sauce...")
        print("Spaghetti is ready to serve!")

# Example usage
ingredients_list = {
    "pasta": {"types": "spaghetti", "amount": 200},
    "tomato sauce": {"amount": 100},
    "garlic": {"amount": 2},
    "olive oil": {"amount": 10}
}
cook_spaghetti(ingredients_list)
