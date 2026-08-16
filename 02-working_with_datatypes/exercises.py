
cooking_instructions = """
Store the multi-line cooking instructions
Step 1: Boil water in a large pot
Step 2: Add pasta and cook for 10 minutes
Step 3: Drain and serve with sauce
"""

print(cooking_instructions)

#REplace method
pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta","fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)

#list
# Create a list of ingredients
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Get the second ingredient for your preview
second_ingredient = ingredients[1]

print(second_ingredient)

# Get every other ingredient starting from the first
alternate_ingredient = ingredients[::2]

print(alternate_ingredient)

# Create a list of ingredient quantities
quantities = [500, 400, 15, 20, 30, 10]

# Extract the last quantity
last_quantity = quantities[-1]


print(last_quantity)
print(ingredients)
print(quantities)


#Dictionary
# Create the recipe dictionary
recipe = {"olive_oil": 30, 
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

print(recipe)


# Create the recipe dictionary
recipe = {"olive_oil": 30,
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

# Add basil to the recipe dictionary
recipe["basil"] = 20

print(recipe)

# Get all ingredient names
ingredient_names = recipe.keys()

# Get all quantities
quantities = recipe.values()

# Get all key-value pairs
recipe_items = recipe.items()

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)