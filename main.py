# ---------------------------- Begin Script ---------------------------- #

# Set 'user' to False so that it will rerun code at end
user = False
while not user:
    # Ask user input for which meal is requested
    user = input("Are you hungry for 'Breakfast', 'Lunch', or 'Dinner'? \n")
    user_lower = user.lower()

    # Connect input to meal
    if user_lower == "breakfast":
        # Still need to connect data in breakfast column.
        print("Still in process, you requested a breakfast restaurant.")
        user = False

    elif user_lower == "lunch":
        # still need to connect data in lunch column
        print("Still in process, you requested a lunch restaurant.")
        user = False

    elif user_lower == "dinner":
        # Still need to connect data in dinner column
        print("Still in process, you selected a dinner restaurant")
        user = False

    else:
        print("Error in module, please run program again")
        user = False