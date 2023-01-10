# ---------------------------- Imports ---------------------------- #
import random

# ---------------------------- Begin Script ---------------------------- #

# Set 'user' to False so that it will rerun code at end
user = False
while not user:
    # Ask user input for which meal is requested
    user = input("Are you hungry for 'Breakfast', 'Lunch', or 'Dinner'? \n")
    user_lower = user.lower()

    # Connect input to meal
    if user_lower == "breakfast":
        def breakfast_choice():
            with open("breakfast.txt", 'r') as b_menu:
                restaurants = b_menu.readlines()
                random_rest = random.choice(restaurants)
            print(random_rest)
            return random_rest
        breakfast_choice()
        user = False
    elif user_lower == "lunch":
        def lunch_choice():
            with open("lunch.txt", 'r') as l_menu:
                restaurants = l_menu.readlines()
                random_rest = random.choice(restaurants)
            print(random_rest)
            return random_rest
        lunch_choice()
        user = False
    elif user_lower == "dinner":
        def dinner_choice():
            with open("dinner.txt", 'r') as d_menu:
                restaurants = d_menu.readlines()
                random_rest = random.choice(restaurants)
            print(random_rest)
            return random_rest
        dinner_choice()
        user = False

    else:
        print("Error in module, please run program again")
        user = False