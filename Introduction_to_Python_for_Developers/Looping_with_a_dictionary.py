recipe = {
    "fusilli": 500,
    "tomatoes": 400,
    "basil": 20,
    "garlic": 15,
    "olive oil": 15,
    "salt": 7
}

# Loop through the recipe dictionary items
for ingredient, qty in recipe.items():
    # Calculate the scaled quantity by multiplying by 2
    scaled_qty = qty * 2
    
    print(ingredient, ":", scaled_qty, "g")
