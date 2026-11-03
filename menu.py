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
    10. Check championship potential
    0. Exit
    """)

def get_action():
    show_menu()
    while True:
        try:
            action =  int(input("Choose an option: "))
            if action < 0 or action > 10:
                print("only numbers between 0 - 10")
                continue
            return action
        except ValueError:
            print("only numbers")

