import validation as v
from inputs import input_positive_integer, input_not_empty_string

def input_new_team_id(teams):
    while True:
        id = input_positive_integer("Enter new team id: ")
        if id not in map(lambda t: t["id"], teams):
            return id
        print("id already exists. Please enter new id!")

def input_new_team_name(teams):
    while True:
        name = input_not_empty_string("Enter new team name: ").lower()
        if name not in map(lambda t: t["name"], teams):
            return name
        print("name already exists. Please enter new name!")

def input_exists_team_id(input_msg, teams):
    while True:
        id = input_positive_integer(input_msg)
        if id in map(lambda t: t["id"], teams):
            return id
        print("id is not exists. Please try again")

def get_team_by_id(id, teams):
    return list(filter(lambda t: t["id"] == id, teams))[0]

def initialize_team(id, name):
    return {
        "id": id,
        "name": name,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

def add_team(teams):
    id = input_new_team_id(teams)
    name = input_new_team_name(teams)
    teams.append(initialize_team(id, name))


def show_all_teams(teams):
    if not teams:
        print("There are no teams yet")

    print()
    for t in teams:
        print(f"{t["id"]}. {t["name"]:<5} {t["played"]} games, {t["points"]} points")


def update_teams(teams, match):
    home_team = list(filter(lambda t: t["id"] == match["home_team_id"], teams))[0]
    away_team = list(filter(lambda t: t["id"] == match["away_team_id"], teams))[0]

    home_team["played"] += 1
    away_team["played"] += 1

    home_team["goals_for"] += match["home_goals"]
    home_team["goals_against"] += match["away_goals"]
    away_team["goals_for"] += match["away_goals"]
    away_team["goals_against"] += match["home_goals"]

    if match["home_goals"] > match["away_goals"]:
        home_team["wins"] += 1
        home_team["points"] += 3
        away_team["losses"] += 1
    elif match["home_goals"] == match["away_goals"]:
        home_team["draws"] += 1
        away_team["draws"] += 1
        home_team["points"] += 1
        away_team["points"] += 1
    else:
        home_team["losses"] += 1
        away_team["wins"] += 1
        away_team["points"] += 3
