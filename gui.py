# ----------------------------------------------- Imports ----------------------------------------------- #
from tkinter import *
# from tkinter import messagebox
import random

# ---------------------------------------------- CONSTANTS ---------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------------------------- WINDOW SETUP ---------------------------------------------- #
window = Tk()
window.title("Restaurant Decider")
window.config(padx=50, pady=50)


# --------------------------------------------- Functions ---------------------------------------------- #
def breakfast_choice():
    with open("breakfast.txt", 'r') as b_menu:
        restaurants = b_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label.config(text=f"\n Your restaurant choice is: {random_rest}")


def lunch_choice():
    with open("lunch.txt", 'r') as l_menu:
        restaurants = l_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label.config(text=f"\n Your restaurant choice is: {random_rest}")


def dinner_choice():
    with open("dinner.txt", 'r') as d_menu:
        restaurants = d_menu.readlines()
        random_rest = random.choice(restaurants)
    return_label.config(text=f"\n Your restaurant choice is: {random_rest}")


# ---------------------------------------------- Main Screen ---------------------------------------------- #

# Top Label(s)
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
return_label = Label(text="\nClick a button above to decide pick a restaurant", font=("Arial", 24))
return_label.grid(row=2, column=0, columnspan=3)

# add_button = Button(text="Add Restaurant", width=15, command=add_menu)
# add_button.grid(row=3, column=0)
# view_button = Button(text="View List", width=15, command=view_options)
# view_button.grid(row=3, column=2)


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
window.mainloop()
