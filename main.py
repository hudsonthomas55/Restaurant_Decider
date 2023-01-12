# ----------------------------------------------- Imports ----------------------------------------------- #
import random


# --------------------------------------------- Functions ----------------------------------------------#
def breakfast_choice():
    with open("breakfast.txt", 'r') as b_menu:
        restaurants = b_menu.readlines()
        random_rest = random.choice(restaurants)
    print(random_rest)
    return random_rest


def lunch_choice():
    with open("lunch.txt", 'r') as l_menu:
        restaurants = l_menu.readlines()
        random_rest = random.choice(restaurants)
    print(random_rest)
    return random_rest


def dinner_choice():
    with open("dinner.txt", 'r') as d_menu:
        restaurants = d_menu.readlines()
        random_rest = random.choice(restaurants)
    print(random_rest)
    return random_rest


def view_options():
    global user
    option_view = input("Do you want to view the options for 'Breakfast', 'Lunch', or 'Dinner'? \nEnter "
                        "'exit' to return to main menu \n").lower()
    if option_view == "breakfast":
        with open("breakfast.txt") as b_menu:
            print(b_menu.read())
            view_options()
    elif option_view == "lunch":
        with open("lunch.txt") as l_menu:
            print(l_menu.read())
            view_options()
    elif option_view == "dinner":
        with open("dinner.txt") as d_menu:
            print(d_menu.read())
            view_options()
    else:
        user = False


# --------------------------------------------- Begin Script ----------------------------------------------#

# Set 'user' to False so that it will rerun code at end
user = False
while not user:
    # Ask user input for which meal is requested
    user = input("Are you hungry for 'Breakfast', 'Lunch', or 'Dinner'? \nIf you wish to view/change the options type "
                 "'Change.'\n").lower()

    # ------------- Return meal options - Actual program
    if user == "breakfast":
        breakfast_choice()
        user = False
    elif user == "lunch":
        lunch_choice()
        user = False
    elif user == "dinner":
        dinner_choice()
        user = False

    # Allow user to view meal options
    elif user == "view":
        view_options()

    # ------------- Allow user to change meal options
    elif user == "change":
        def make_change():
            change = input("Welcome to the change menu. Would you like to 'view', 'add', or 'delete' a restaurant? "
                           "\n").lower()
            # View meal options
            if change == "view":
                view_options()

            # ------------- Allow user to add meal options
            elif change == "add":
                def change_list():
                    global user
                    option_change = input("Which list would you like to add to? 'Breakfast,' 'Lunch,' or 'Dinner? "
                                          "\n").lower()
                    if option_change == "breakfast":
                        with open("breakfast.txt") as b_menu:
                            print(f"your current list is: \n {b_menu.read()}")
                        new_restaurant = input("\n \n What is the name of the restaurant you wish to add? \n")
                        b_menu = open("breakfast.txt", "a")  # append mode
                        b_menu.write(f"\n{new_restaurant}")
                        b_menu.close()
                        with open("breakfast.txt") as b_menu:
                            print(f"your updated list is: \n {b_menu.read()}")
                        change_list()
                    elif option_change == "lunch":
                        with open("lunch.txt") as l_menu:
                            print(f"your current list is: \n {l_menu.read()}")
                        new_restaurant = input("\n \n What is the name of the restaurant you wish to add? \n")
                        l_menu = open("lunch.txt", "a")  # append mode
                        l_menu.write(f"\n{new_restaurant}")
                        l_menu.close()
                        with open("lunch.txt") as l_menu:
                            print(f"your updated list is: \n {l_menu.read()}")
                        change_list()
                    elif option_change == "dinner":
                        with open("dinner.txt") as d_menu:
                            print(f"your current list is: \n {d_menu.read()}")
                        new_restaurant = input("\n \n What is the name of the restaurant you wish to add? \n")
                        d_menu = open("dinner.txt", "a")  # append mode
                        d_menu.write(f"\n{new_restaurant}")
                        d_menu.close()
                        with open("dinner.txt") as d_menu:
                            print(f"your updated list is: \n {d_menu.read()}")
                        change_list()
                    else:
                        user = False

                change_list()

            # ------------------------------------ Delete Options ------------------------------------ #
            elif change == "delete":
                pass
                # TODO: Add function for deleting items from lists


        make_change()

    else:
        print("Error, please try again")
        user = False
