# Check if you have enough tomatoes for the full party

pantry_stock = {"tomatoes": 1000}
ingredients_needed = {"tomatoes": 80}

if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")
    
# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800:
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
    
#for loop through a list
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through each ingredient in the list
for item in ingredients:
    print(item)
# Iterate over the number of ingredients
for item in range(1,7):
    print("Adding ingredient", item)
    
quantities = [500, 400, 20, 15, 15, 7]


#Conditional looping with lists
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

#Looping with dictionary
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
    
    
#While loop
