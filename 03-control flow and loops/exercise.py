# ============================================================
# IF / ELIF / ELSE
# ============================================================

# Check if you have enough tomatoes for the full party

pantry_stocks = {"tomatoes": 1000}
ingredients_needed = {"tomatoes": 80}

if pantry_stocks["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")
    
# Check if you have enough for a smaller gathering
elif pantry_stocks["tomatoes"] >= 800:
    print("Only enough tomatoes for a smaller gathering.") 

else:
    print("Need to buy tomatoes before the party.")
    

# Check if you have exactly the right amount of basil

basil_grams = 50
required_basil = 50

if basil_grams == required_basil:
    print('Perfect! You have exactly the right amount of basil.')

else:
    print('You need to adjust your basil quantity.')
    

# ============================================================
# FOR LOOPS
# ============================================================

# For loop through a list

ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through each ingredient in the list
for item in ingredients:
    print(item)


# Iterate over the number of ingredients

for item in range(1,7):
    print("Adding ingredient", item)
    

quantities = [500, 400, 20, 15, 15, 7]


# Conditional looping with lists

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


# Looping with dictionary

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
    
    
# ============================================================
# WHILE LOOPS
# ============================================================

# While loop

total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop

total_confirmations = 10
guest_count = 0

while guest_count < total_confirmations:
    guest_count = guest_count + 1
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")


# Conditional while loops

total_ingredients = 7
ingredients_checked = 0

# Set up the loop

while ingredients_checked < total_ingredients:

    # Increment the counter
    ingredients_checked += 1

    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")

    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")

    else:
        print("All ingredients verified!")
       

# ============================================================
# LISTS / APPENDING TO A LIST
# ============================================================

# Appending to a list

recipe = {
    "pasta": 500,
    "tomatoes": 400,
    "garlic": 20,
    "olive_oil": 15
}

pantry_stock = {
    "pasta": 400,
    "tomatoes": 500,
    "garlic": 10,
    "olive_oil": 5
}

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


# Count how many items to buy

items_to_buy = 0

for item in shopping_list:
    items_to_buy += 1

# Display results
print(items_to_buy)
print(shopping_list)


# ============================================================
# RECIPE SCALER
# ============================================================

# Building the recipe scaler

scale_factor = 2

pantry = {
    "pasta": 500,
    "tomatoes": 300,
    "garlic": 10
}

shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    print(ingredient)


# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():

    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor
    
    
    # Check if we need to buy this ingredient
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)