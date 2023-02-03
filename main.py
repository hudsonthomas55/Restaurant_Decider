# ----------------------------------------------- Imports ----------------------------------------------- #
from tkinter import *
import random

# ---------------------------------------------- WINDOW SETUP ---------------------------------------------- #
window = Tk()
window.minsize(width=700, height=500)
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


    # View buttons and options
    breakfast_view_button = Button(text="View Restaurant Options", width=15, command=view_menu)
    breakfast_view_button.grid(row=3, column=0)


# ---------------------------------------------- View Screen ---------------------------------------------- #
def view_menu():
    clear_frame()
    # TOP BUTTONS
    back_button = Button(text="Go Back", width=5, command=main_screen)
    back_button.grid(row=0, column=0)
    add_button = Button(text="Add Restaurant", width=10, command=add_menu)
    add_button.grid(row=0, column=2)
    # HEADER LABEL
    header_label = Label(text="\n Welcome to the view menu! See below list of restaurant options: \n", font=("Arial",
                                                                                                             30))
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
        option_label.grid(row=(return_number + 2), column=0, sticky="w")
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
        option_label.grid(row=(return_number + 2), column=1, sticky="w")
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
        option_label.grid(row=(return_number + 2), column=2, sticky="w")
        return_number += 1


# ---------------------------------------------- Add Screen ---------------------------------------------- #
def add_menu():
    clear_frame()

    # Make Submit button work
    def submit_add_button():
        new_restaurant = restaurant_name.get()
        breakfast_check = b_checked_state.get()
        lunch_check = l_checked_state.get()
        dinner_check = d_checked_state.get()

        if breakfast_check == 1:
            with open("breakfast.txt", 'a') as breakfast_menu:
                breakfast_menu.write(f"\n{new_restaurant}")
            add_menu()
        elif lunch_check == 1:
            with open("lunch.txt", 'a') as lunch_menu:
                lunch_menu.write(f"\n{new_restaurant}")
            add_menu()
        elif dinner_check == 1:
            with open("dinner.txt", 'a') as dinner_menu:
                dinner_menu.write(f"\n{new_restaurant}")
            add_menu()

    # TOP BUTTONS
    back_button = Button(text="Main Menu", width=5, command=main_screen)
    back_button.grid(row=0, column=0)
    add_button = Button(text="Add Restaurant", width=10)  # Add command to this line
    add_button.grid(row=0, column=2)

    # ADD SECTION
    add_label = Label(text="\n Add your new restaurant below: \n", font=("Arial", 20))
    add_label.grid(row=1, column=0, columnspan=3)
    # ENTRY BOX
    restaurant_label = Label(text="Restaurant Name:")
    restaurant_label.grid(row=2, column=0)
    restaurant_name = Entry(width=30)
    restaurant_name.insert(END, string="Be mindful of spelling and capitalization")
    restaurant_name.grid(row=2, column=1)
    # CHECKBOXES
    check_label = Label(text="This restaurant serves:")
    check_label.grid(row=3, column=1)
    b_checked_state = IntVar()
    b_checkbox = Checkbutton(text="Breakfast", variable=b_checked_state)
    b_checkbox.grid(row=4, column=0)
    l_checked_state = IntVar()
    l_checkbox = Checkbutton(text="Lunch", variable=l_checked_state)
    l_checkbox.grid(row=4, column=1)
    d_checked_state = IntVar()
    d_checkbox = Checkbutton(text="Dinner", variable=d_checked_state)
    d_checkbox.grid(row=4, column=2)
    # SUBMIT BUTTON
    submit_button = Button(text="Submit", width=15, command=submit_add_button)
    submit_button.grid(row=5, column=1)


    # HEADER LABEL
    header_label = Label(text="\nSee below list of current restaurant options: ", font=("Arial", 30))
    header_label.grid(row=6, column=0, columnspan=3)

    # BREAKFAST SECTION
    breakfast_label = Label(text="Breakfast: \n", font=("Arial", 16))
    breakfast_label.grid(row=7, column=0)
    return_number = 1
    breakfast_option_list = []
    with open("breakfast.txt") as b_menu:
        for option in b_menu.readlines():
            breakfast_option_list.append(option)
    for restaurant in breakfast_option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 7), column=0, sticky="w")
        return_number += 1

    # LUNCH SECTION
    lunch_label = Label(text="Lunch: \n", font=("Arial", 16))
    lunch_label.grid(row=7, column=1)
    return_number = 1
    lunch_option_list = []
    with open("lunch.txt") as l_menu:
        for option in l_menu.readlines():
            lunch_option_list.append(option)
    for restaurant in lunch_option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 7), column=1, sticky="w")
        return_number += 1

    # DINNER SECTION
    dinner_label = Label(text="Dinner: \n", font=("Arial", 16))
    dinner_label.grid(row=7, column=2)
    return_number = 1
    option_list = []
    with open("dinner.txt") as d_menu:
        for option in d_menu.readlines():
            option_list.append(option)
    for restaurant in option_list:
        option_label = Label(text=f"{return_number}. {restaurant}", font=("Arial", 12))
        option_label.grid(row=(return_number + 7), column=2, sticky="w")
        return_number += 1




# ---------------------------------------------- KEEP WINDOW OPEN ---------------------------------------------- #
main_screen()

window.mainloop()
