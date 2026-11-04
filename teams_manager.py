import validation as v
from inputs import input_positive_integer, input_not_empty_string

def input_new_id(teams):
    while True:
        id = input_positive_integer("Enter new team id: ")
        if id not in map(lambda t: t["id"], teams):
            return id
        print("id already exists. Please enter new id!")

def input_new_name(teams):
    while True:
        name = input_not_empty_string("Enter new team name: ").lower()
        if name not in map(lambda t: t["name"], teams):
            return name
        print("name already exists. Please enter new name!")

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
    id = input_new_id(teams)
    name = input_new_name(teams)
    teams.append(initialize_team(id, name))


def show_all_teams(teams):
    if not teams:
        print("There are no teams yet")

    print()
    for t in teams:
        print(f"{t["id"]}. {t["name"]:<5} {t["played"]} games, {t["points"]} points")


def update_teams(teams, match):
    for t in teams:
        if t["id"] == match["home_team_id"]:
            t["played"] += 1
            if match["home_goals"] > match["away_goals"]:
                t["wins"] += 1
                t["points"] += 3
            elif match["home_goals"] == match["away_goals"]:
                t["draws"] += 1
                t["points"] += 1
            else:
                t["losses"] += 1
            t["goals_for"] += match["home_goals"]
            t["goals_against"] += match["away_goals"]
            break

    for t in teams:
        if t["id"] == match["away_team_id"]:
            t["played"] += 1
            if match["away_goals"] > match["home_goals"]:
                t["wins"] += 1
                t["points"] += 3
            elif match["away_goals"] == match["home_goals"]:
                t["draws"] += 1
                t["points"] += 1
            else:
                t["losses"] += 1
            t["goals_for"] += match["away_goals"]
            t["goals_against"] += match["home_goals"]
            break



    # home_team = filter(lambda t: t["id"] == match["home_team_id"], teams)
    # away_team = filter(lambda t: t["id"] == match["away_team_id"], teams)

    # for t in teams:
    #     if t["id"] == match["home_team_id"]:
    #         home_team = t
    #         break
    
    # for t in teams:
    #     if t["id"] == match["away_team_id"]:
    #         away_team = t
    #         break

    # home_team["played"] += 1
    # away_team["played"] += 1

        
    # if match["home_goals"] > match["away_goals"]:
    #     t["wins"] += 1
    #     t["points"] += 3
    # elif match["home_goals"] == match["away_goals"]:
    #     t["draws"] += 1
    #     t["points"] += 1
    # else:
    #     t["losses"] += 1
    # t["goals_for"] += match["home_goals"]
    # t["goals_against"] += match["away_goals"]
    
