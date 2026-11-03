from prettytable import PrettyTable

t = PrettyTable(['Name', 'Games', 'Wins', 'Draws', 'Losses', 'Goals For', 'Goals Against', 'Gap', 'Points'])

def sort_teams(teams):
    return sorted(teams, 
                key=lambda t: (t["points"], t["goals_for"] - t["goals_against"], t["goals_for"], t["name"]), 
                reverse=True)


def show_standing(teams, matches):
    if not matches:
        print("There are no matches yet")
        return
    
    standing = sort_teams(teams)

    for s in standing:
        t.add_row([s["name"], s["played"], s["wins"], s["draws"], s["losses"], s["goals_for"], s["goals_against"], s["goals_for"] - s["goals_against"], s["points"]])

    print()
    print(t)

def show_leading_team(teams, matches):
    if not matches:
        print("There are no matches yet")
        return
    
    print(f"the best team is: {max(teams)[0]["name"]}")

