quantities = [500, 400, 20, 15, 15, 7]

# Loop through each quantity in the recipe
for qty in quantities:
    # Check if it's a large quantity (400g or more)
    if qty >= 400:
        print('Large quantity')
    # Check if it's a medium quantity (200g or more)
    elif qty >= 200:
        print('Medium quantity')
    # Otherwise it's a small quantity
    else:
        print('Small quantity')
