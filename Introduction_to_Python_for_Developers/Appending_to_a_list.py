# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", shopping_list)
