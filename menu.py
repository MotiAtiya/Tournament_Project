import logging
from inputs import input_not_negative_integer

def show_menu():
    print("""
    ========== TOURNAMENT MANAGER ==========
    1. Add team
    2. Show all teams
    3. Add match result
    4. Show standings
    5. Show leading team
    6. Show best attacking team
    7. Show team success rate
    8. Show teams without wins
    9. Show tournament summary
    0. Exit
    """)

def get_action():
    show_menu()
    while True:
        action = input_not_negative_integer("Choose an option (0-9):")
        if  0 <= action <= 9:
            return action
        
        print("Enter only numbers between 0 - 9")
        logging.info("Wrong input: The user selected an action that does not exist in the menu")

