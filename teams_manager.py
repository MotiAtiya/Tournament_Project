import validation as v

def input_id():
    while True:
        try:
            id = int(input("Enter team id: ").strip())
            if v.is_positive_integer_number(id):
                return id
            print("Please enter only a positive integer number!") 
        except ValueError:
            print("Please enter only a number!")


def input_name():
    while True:
        name = input("Enter team name: ").strip().lower()
        if v.is_non_empty_string(name):
            return name
        print("Please enter only a non-empay name!") 


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
    while True:
        id = input_id()
        if id not in map(lambda t: t["id"], teams):
            break
        print("id already exists. Please enter new id!")

    while True:
        name = input_name()
        if name not in map(lambda t: t["name"], teams):
            break
        print("name already exists. Please enter new name!")

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
    
