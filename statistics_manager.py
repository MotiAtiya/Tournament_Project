from prettytable import PrettyTable
from teams_manager import input_exists_team_id, get_team_by_id
from printer import print_title, print_no_matches_yet, print_no_teams_yet
from io_manager import load_data, TEAMS_PATH, MATCHES_PATH

def sort_teams(teams):
    return sorted(teams, key=lambda t: (-t["points"], -(t["goals_for"] - t["goals_against"]), -t["goals_for"], t["name"]))

def show_standing():
    teams = load_data(TEAMS_PATH)
    matches = load_data(MATCHES_PATH)
    if not matches:
        print_no_matches_yet()
        return
    
    print_title("SHOW STANDING")
    standing = sort_teams(teams)

    table = PrettyTable(['Name', 'Games', 'Wins', 'Draws', 'Losses', 'Goals For', 'Goals Against', 'Gap', 'Points'])
    for s in standing:
        table.add_row([s["name"], s["played"], s["wins"], s["draws"], s["losses"], s["goals_for"], s["goals_against"], s["goals_for"] - s["goals_against"], s["points"]])

    print(table)

def get_leading_team(teams):
    return sort_teams(teams)[0]

def show_leading_team():
    teams = load_data(TEAMS_PATH)
    matches = load_data(MATCHES_PATH)
    if not matches:
        print_no_matches_yet()
        return

    print_title("SHOW LEADING TEAM")
    print(f"the best team is: {get_leading_team(teams)["name"]}")

def show_best_attacking_team():
    teams = load_data(TEAMS_PATH)
    if not teams:
        print_no_teams_yet()
        return
    max_goals_for_team = max(teams, key=lambda t: t["goals_for"])
    max_goals_for_value = max_goals_for_team["goals_for"]
    best_teams = filter(lambda t: t["goals_for"] == max_goals_for_value, teams)

    print_title("SHOW BEST ATTACKING TEAMS")
    for b in best_teams:
        print(f"best teams goals for: {b["name"]}, with {max_goals_for_value} goals for")

def show_team_success_rate():
    teams = load_data(TEAMS_PATH)
    if not teams:
        print_no_teams_yet()
        return
    team_id = input_exists_team_id("Enter team id: ",teams)
    team = get_team_by_id(team_id, teams)
    if team["played"] == 0:
        print_no_matches_yet()
        return
    
    rate = round(team["points"] / (team["played"] * 3) * 100, 2)
    print_title("SHOW TEAM SUCCESS RATE")
    print("team success rate:", rate)

def show_teams_without_wins():
    teams = load_data(TEAMS_PATH)
    if not teams:
        print_no_teams_yet()
        return
    teams_without_wins = list(filter(lambda t: (t["played"] > 0 and t["wins"] == 0), teams))
    if not teams_without_wins:
        print("There are no teams without wins!")
        return
    
    print_title("TEAMS WITHOUT WINS")
    for t in teams_without_wins:
        print(f"{t["name"]}: played {t["played"]} matches, earned {t["points"]} points")


def show_tournament_summary():
    teams = load_data(TEAMS_PATH)
    matches = load_data(MATCHES_PATH)
    if not matches:
        print_no_matches_yet()
        return
    if not teams:
        print_no_teams_yet()
        return

    num_of_teams = len(teams)
    num_of_matches = len(matches)
    total_goals = sum(team["goals_for"] for team in teams)
    average_goals_per_match = total_goals / num_of_matches
    num_of_draws = round(sum(team["draws"] for team in teams) / 2)
    leading_tame_name = get_leading_team(teams)["name"]

    print_title("TOURNAMENT SUMMARY")
    print(num_of_teams, "teams")
    print(num_of_matches, "matches")
    print(total_goals, "goals in total")
    print(average_goals_per_match, "average goals per match")
    print(num_of_draws, "matches ended in a draw")
    print(leading_tame_name, "is the best team")


def check_championship_potential():
    teams = load_data(TEAMS_PATH)
    if not teams:
        print_no_teams_yet()
        return

    team_id = input_exists_team_id("Enter team id: ",teams)
    team = get_team_by_id(team_id, teams)

    remain_games = len(teams) - 1 - team["played"]
    maximum_points = team["points"] + remain_games * 3
    
    print_title("Check Championship Potential")
    if maximum_points > max(teams, key=lambda t: t["points"])["points"]:
        print(f"this team can be the championship in potential. it can achive {maximum_points} points")
    else:
        print(f"this team can not be the championship. it can achive only {maximum_points} points")
