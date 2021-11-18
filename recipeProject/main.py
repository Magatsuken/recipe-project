import json


# Test that overwrites file with a recipe
def write_recipe(recipe):
    with open("recipes.json", 'w') as file:
        recipe = json.dump(recipe, file)
        file.write("\n")
        file.close()


# Prints all recipes
def print_all_recipes():
    # Initializes a blank list
    recipe_list = []
    # Opens file as readable
    with open("recipes.json", 'r') as file:
        # For loop, each json_obj is read as a dict and appended to a list
        for json_obj in file:
            recipe_dict = json.loads(json_obj)
            recipe_list.append(recipe_dict)
        # For loop, each iteration prints out a whole recipe
        for recipe in recipe_list:
            print("Name: \n" + recipe["name"])
            print("\nIngredients: ")
            # Grabs a list of dict items, for loop goes through each item and prints out the key and value of the dict
            dic_items = recipe["ingredients"]
            for i in dic_items:
                for k, v in i.items():
                    print(k + ": " + v)
            print("\nCook Time: " + recipe["cook time"])
            print("\nMethod: " + recipe["method"])
            # Neatly prints out instructions by step number, j is step 1 and is incremented each loop
            print("\nInstructions: ")
            j = 1
            for i in recipe["instructions"]:
                print(str(j) + ". " + i)
                j += 1
            print("\n")
        file.close()


# Appends a recipe to the recipe list (recipes.json file)
# Opens file in append mode
# Creates a json object that is appended
# Adds a new line and closes the file as good practice
def append_recipe(recipe):
    with open("recipes.json", 'a') as file:
        recipe_json = json.dump(recipe, file)
        file.write("\n")
        file.close()


# Displays the main menu
def display_main_menu():
    print("1. View all recipes")
    print("2. Search for a recipe")
    print("3. Add a recipe")
    print("4. Quit app")


# Displays the search menu
def display_search_menu():
    print("1. Search by name")
    print("2. Search by ingredients")
    print("3. Search by cook time")
    print("4. Search by method")
    print("5. Back to previous menu")


# Adds a recipe by asking the user to input name, ingredients, cook time, method, and instructions
# A new recipe is created using the variables above and is appended to the recipes.json file
def add_recipe():
    name = get_recipe_name()
    ingredients = get_recipe_ingredients()
    cook_time = get_recipe_cook_time()
    method = get_recipe_method()
    instructions = get_recipe_instructions()
    # The new recipe is stored as a dict which can be used as a json object. json takes dicts
    new_recipe = {"name": name, "ingredients": ingredients, "cook time": cook_time, "method": method,
                  "instructions": instructions}
    append_recipe(new_recipe)


# Gets the recipe name from the user
def get_recipe_name():
    name = input("What is the recipe name? \n")
    return name


# Gets the ingredients from the user
def get_recipe_ingredients():
    # Initializes variables
    ingredients = []
    ingredient = {}
    k = ""
    v = ""
    # While loop where if k is not "done", it will keep looping
    # If k == "done", loop breaks and the ingredient dict is not updated
    # k = key and v = value, k and v are updated to the ingredient dict
    # When the loop breaks, the dict is appended to the ingredients list
    while k != "done":
        k = input("List an ingredient? Type 'done' if done. \n").lower()
        if k == "done":
            break
        v = input("List the quantity, unit, and preparation. IE: 6 strips, chopped: ")
        ingredient.update({k: v})
    ingredients.append(ingredient)
    return ingredients


# Gets the recipe cook time from the user in hours
def get_recipe_cook_time():
    cook_time = input("What is the cook time in hours? \n") + " hours"
    return cook_time


# Gets the recipe cooking method from the user
def get_recipe_method():
    method = input("What is the cooking method? \n").lower()
    return method


# Gets instructions on how to make the recipe from the user
def get_recipe_instructions():
    # Initializes variables
    instructions = []
    i = ""
    # While loop where if i is not "done", it will keep looping
    # i = instruction one step at a time
    # i is appended to the instructions list
    while i != "done":
        i = input("List your instructions step by step. Type 'done if done.\n")
        if i == "done":
            break
        instructions.append(i)
    return instructions


# Searches for a recipe name based off of what the user wants to search for
def search_recipe_name(name):
    # Initializes a blank list
    recipe_list = []
    # Opens the recipes.json file as readable
    with open("recipes.json", 'r') as file:
        # For loop, each json_obj is read as a dict and appended to a list
        for json_obj in file:
            recipe_dict = json.loads(json_obj)
            recipe_list.append(recipe_dict)
        # This checks through each recipe, if the recipe name matches the name the user searched for
        # It returns the whole recipe if a recipe is found
        for recipe in recipe_list:
            if name == recipe["name"]:
                print("Name: \n" + recipe["name"])
                print("\nIngredients: ")
                dic_items = recipe["ingredients"]
                for i in dic_items:
                    for k, v in i.items():
                        print(k + ": " + v)
                print("\nCook Time: " + recipe["cook time"])
                print("\nMethod: " + recipe["method"])
                print("\nInstructions: ")
                j = 1
                for i in recipe["instructions"]:
                    print(str(j) + ". " + i)
                    j += 1
                print("\n")
        file.close()


# Searches for a single ingredient in a recipe based off of what the user searches for
def search_recipe_ingredient(ingredient):
    # Initializes a blank list
    recipe_list = []
    # Opens the recipes.json file as readable
    with open("recipes.json", 'r') as file:
        # For loop, each json_obj is read as a dict and appended to a list
        for json_obj in file:
            recipe_dict = json.loads(json_obj)
            recipe_list.append(recipe_dict)
        # This checks if a single ingredient is in a recipe
        # It returns the whole recipe if the same ingredient is found
        for recipe in recipe_list:
            dic_items = recipe["ingredients"]
            for i in dic_items:
                for k, v in i.items():
                    if ingredient == k:
                        print("Name: \n" + recipe["name"])
                        print("\nIngredients: ")
                        dic_items = recipe["ingredients"]
                        for i in dic_items:
                            for k, v in i.items():
                                print(k + ": " + v)
                        print("\nCook Time: " + recipe["cook time"])
                        print("\nMethod: " + recipe["method"])
                        print("\nInstructions: ")
                        j = 1
                        for i in recipe["instructions"]:
                            print(str(j) + ". " + i)
                            j += 1
                        print("\n")
        file.close()


# Searches for the cook time in a recipe based off of what the user searches for
def search_recipe_cook_time(time):
    # Initializes a blank list
    recipe_list = []
    # Opens the recipes.json file as readable
    with open("recipes.json", 'r') as file:
        # For loop, each json_obj is read as a dict and appended to a list
        for json_obj in file:
            recipe_dict = json.loads(json_obj)
            recipe_list.append(recipe_dict)
            # This checks if the cook time the user searched for is in the recipe
            # It returns the whole recipe if the same cook time is found
        for recipe in recipe_list:
            if time == recipe["cook time"]:
                print("Name: \n" + recipe["name"])
                print("\nIngredients: ")
                dic_items = recipe["ingredients"]
                for i in dic_items:
                    for k, v in i.items():
                        print(k + ": " + v)
                print("\nCook Time: " + recipe["cook time"])
                print("\nMethod: " + recipe["method"])
                print("\nInstructions: ")
                j = 1
                for i in recipe["instructions"]:
                    print(str(j) + ". " + i)
                    j += 1
                print("\n")
        file.close()


# Searches for the cooking method in a recipe based off of what the user searches for
def search_recipe_method(method):
    # Initializes a blank list
    recipe_list = []
    # Opens the recipes.json file as readable
    with open("recipes.json", 'r') as file:
        # For loop, each json_obj is read as a dict and appended to a list
        for json_obj in file:
            recipeDict = json.loads(json_obj)
            recipe_list.append(recipeDict)
        # This checks if the cooking method the user searched for is in the recipe
        # It returns the whole recipe if the same cooking method is found
        for recipe in recipe_list:
            if method == recipe["method"]:
                print("Name: \n" + recipe["name"])
                print("\nIngredients: ")
                dic_items = recipe["ingredients"]
                for i in dic_items:
                    for k, v in i.items():
                        print(k + ": " + v)
                print("\nCook Time: " + recipe["cook time"])
                print("\nMethod: " + recipe["method"])
                print("\nInstructions: ")
                j = 1
                for i in recipe["instructions"]:
                    print(str(j) + ". " + i)
                    j += 1
                print("\n")
        file.close()


# Main menu function which checks for valid input
def main_menu_input():
    main_menu_input = input("\nChoose a number: ")
    while main_menu_input != "4":
        if main_menu_input == "1":
            print_all_recipes()
        elif main_menu_input == "2":
            display_search_menu()
            search_menu_input()
        elif main_menu_input == "3":
            add_recipe()
        else:
            print("Invalid option.")
        display_main_menu()
        main_menu_input = input("\nChoose a number: ")
    print("Exiting program.")


# Search menu function which checks for valid input
def search_menu_input():
    search_menu_input = input("\nChoose a number: ")
    while search_menu_input != "5":
        if search_menu_input == "1":
            name = input("What is the recipe name? \n").lower()
            search_recipe_name(name)
        elif search_menu_input == "2":
            ingredient = input("What is the recipe ingredient? \n").lower()
            search_recipe_ingredient(ingredient)
        elif search_menu_input == "3":
            time = input("What is the cook time in hours? \n") + " hours"
            search_recipe_cook_time(time)
        elif search_menu_input == "4":
            method = input("What is the cooking method? \n").lower()
            search_recipe_method(method)
        else:
            print("Invalid option.")
        display_search_menu()
        search_menu_input = input("\nChoose a number: ")
    print("Exiting program.")


display_main_menu()
main_menu_input()
