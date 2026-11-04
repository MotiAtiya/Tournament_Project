from inputs import input_positive_integer
import validation as v
from teams_manager import update_teams, input_exists_team_id

def input_home_and_away_teams_id(teams, matches):
    while True:
        home_team_id = input_exists_team_id("Enter home team id: ", teams)
        away_team_id = input_exists_team_id("Enter away team id: ", teams)
        if away_team_id == home_team_id:
            print("Please enter different id for away team!")
            continue

        return home_team_id, away_team_id
    

def have_played_before(matches, home_team_id, away_team_id):
    for m in matches:
        if (m["home_team_id"] == home_team_id or m["home_team_id"] == away_team_id) and \
            (m["away_team_id"] == away_team_id or m["away_team_id"] == home_team_id):
            return True
    return False

def input_team_goals(team_kind):
    while True:
        try:
            goals = int(input(f"Enter the numbers of goals for {team_kind} team: ").strip())
            if v.is_not_negative_integer_number(goals):
                return goals
            print("Please enter only a not negative integer number!") 
        except ValueError:
            print("Please enter only a number!")

def create_match(mathces, home_id, away_id, home_goals, away_goals):
    return {
        "home_team_id": home_id,
        "away_team_id": away_id,
        "home_goals": home_goals,
        "away_goals": away_goals
    }

def add_match_result(teams, matches):
    while True:
        home_team_id, away_team_id = input_home_and_away_teams_id(teams, matches)
        if have_played_before(matches, home_team_id, away_team_id):
            print("These teams already played before. Please enter new teams")
        break

    home_team_goals = input_team_goals("home")
    away_team_goals = input_team_goals("away")

    new_match = create_match(matches, home_team_id, away_team_id, home_team_goals, away_team_goals)
    matches.append(new_match)
    update_teams(teams, new_match)

