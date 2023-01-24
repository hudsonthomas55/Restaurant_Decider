# ----------------------------------------------- Imports ----------------------------------------------- #
from tkinter import *
# from tkinter import messagebox
import random

# ---------------------------------------------- CONSTANTS ---------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------------------------- WINDOW SETUP ---------------------------------------------- #
window = Tk()
window.minsize(width=600, height=400)
window.title("Restaurant Decider")
window.config(padx=50, pady=50)


# --------------------------------------------- Functions ---------------------------------------------- #
def breakfast_choice():
    clear_frame()
    main_screen()
    with open("breakfast.txt", 'r') as b_menu:
        restaurants = b_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label = Label(text=f"\n Your restaurant choice is: {random_rest} \n\n", font=("Arial", 24))
    return_label.grid(row=2, column=0, columnspan=3)


def lunch_choice():
    clear_frame()
    main_screen()
    with open("lunch.txt", 'r') as l_menu:
        restaurants = l_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label = Label(text=f"\n Your restaurant choice is: {random_rest} \n\n", font=("Arial", 24))
    return_label.grid(row=2, column=0, columnspan=3)


def dinner_choice():
    clear_frame()
    main_screen()
    with open("dinner.txt", 'r') as d_menu:
        restaurants = d_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label = Label(text=f"\n Your restaurant choice is: {random_rest} \n\n", font=("Arial", 24))
    return_label.grid(row=2, column=0, columnspan=3)


def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()


# ---------------------------------------------- Main Screen ---------------------------------------------- #
def main_screen():
    clear_frame()
    welcome_label = Label(text="Welcome! \n What meal are you hungry for? \n", font=("Arial", 30))
    welcome_label.grid(row=0, column=0, columnspan=3)

    # Meal Buttons
    breakfast_button = Button(text="Breakfast", width=15, command=breakfast_choice)
    breakfast_button.grid(row=1, column=0)
    lunch_button = Button(text="Lunch", width=15, command=lunch_choice)
    lunch_button.grid(row=1, column=1)
    dinner_button = Button(text="Dinner", width=15, command=dinner_choice)
    dinner_button.grid(row=1, column=2)

    # Bottom Label(s)
    return_label = Label(text="\n\n\n", font=("Arial", 24))
    return_label.grid(row=2, column=0, columnspan=3)

    # add_button = Button(text="Add Restaurant", width=15, command=add_menu)
    # add_button.grid(row=3, column=0)

    # View buttons and options
    breakfast_view_button = Button(text="View Breakfast Options", width=15, command=view_menu)
    breakfast_view_button.grid(row=3, column=0)


# ---------------------------------------------- View Screen ---------------------------------------------- #
def view_menu():
    clear_frame()
    # BACK BUTTON
    back_button = Button(text="Go Back", width=5, command=main_screen)
    back_button.grid(row=0, column=0)
    # HEADER LABEL
    header_label = Label(text="Welcome to the view menu! See below list of restaurant options: \n", font=("Arial", 30))
    header_label.grid(row=1, column=0, columnspan=3)

    # BREAKFAST SECTION
    breakfast_label = Label(text="Breakfast: \n")
    breakfast_label.grid(row=2, column=0)
    return_number = 1
    breakfast_option_list = []
    with open("breakfast.txt") as b_menu:
        for option in b_menu.readlines():
            breakfast_option_list.append(option)
    for restaurant in breakfast_option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 2), column=0)
        return_number += 1

    # LUNCH SECTION
    lunch_label = Label(text="Lunch: \n")
    lunch_label.grid(row=2, column=1)
    return_number = 1
    lunch_option_list = []
    with open("lunch.txt") as l_menu:
        for option in l_menu.readlines():
            lunch_option_list.append(option)
    for restaurant in lunch_option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 2), column=1)
        return_number += 1

    # DINNER SECTION
    dinner_label = Label(text="Dinner: \n")
    dinner_label.grid(row=2, column=2)
    return_number = 1
    option_list = []
    with open("dinner.txt") as d_menu:
        for option in d_menu.readlines():
            option_list.append(option)
    for restaurant in option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 2), column=2)
        return_number += 1


# ---------------------------------------------- Add Screen ---------------------------------------------- #
# def add_menu():
#
#     main_label = Label(text="Welcome to the add menu. \n What meal does the restaurant serve? \n", font=("Arial", 30))
#     main_label.grid(row=0, column=0, columnspan=3)
#
#
#     # Create new buttons for add
#     breakfast_add_button = Button(text="Breakfast", width=15, command=breakfast_add)
#     breakfast_add_button.grid(row=1, column=0)
#     lunch_add_button = Button(text="Lunch", width=15, command=lunch_add)
#     lunch_add_button.grid(row=1, column=1)
#     dinner_add_button = Button(text="Dinner", width=15, command=dinner_add)
#     dinner_add_button.grid(row=1, column=2)
#
#     back_button = Button(text="Back to Menu", width=30, command=main_screen())
#     back_button.grid(row=2, column=0, columnspan=3)


# ---------------------------------------------- KEEP WINDOW OPEN ---------------------------------------------- #
main_screen()

window.mainloop()
