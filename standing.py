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
    
    print(f"the best team is: {sort_teams(teams)[0]["name"]}")


def show_best_attacking_team(teams):
    max_goals_for_team = max(teams, key=lambda t: t["goals_for"])
    max_goals_for_value = max_goals_for_team["goals_for"]
    best_teams = filter(lambda t: t["goals_for"] == max_goals_for_value, teams)
    for b in best_teams:
        print(f"best teams goals for: {b["name"]}, with {max_goals_for_value} goals for")

# def show_team_success_rate(teams):
#     team_id = int(input("Enter Team ID: "))
#     team = filter(lambda t: t["id"] == team_id, teams)
#     print(team)
#     print(f"Team Success Rate: {team["points"] / (team["played"] * 3) * 100}")

