from printer import print_title
import validation as v
from teams_manager import update_teams, input_exists_team_id
from inputs import input_positive_integer, input_not_negative_integer

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

def create_match(home_id, away_id, home_goals, away_goals):
    return {
        "home_team_id": home_id,
        "away_team_id": away_id,
        "home_goals": home_goals,
        "away_goals": away_goals
    }

def add_match_result(teams, matches):
    print_title("ADD MATCH RESULT")
    while True:
        home_team_id, away_team_id = input_home_and_away_teams_id(teams, matches)
        if have_played_before(matches, home_team_id, away_team_id):
            print("These teams already played before. Please enter new teams")
        break

    home_team_goals = input_not_negative_integer(f"Enter the numbers of goals for home team: ")
    away_team_goals = input_not_negative_integer(f"Enter the numbers of goals for away team: ")

    new_match = create_match(home_team_id, away_team_id, home_team_goals, away_team_goals)
    matches.append(new_match)
    update_teams(teams, new_match)

