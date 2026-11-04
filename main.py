from menu import get_action
from teams_manager import add_team, show_all_teams
from matches_manager import add_match_result
from standing import show_standing, show_leading_team, show_best_attacking_team

def main():
    teams = []
    matches = []
    while True:
        action = get_action()
        if action == 0:
            return

        if action == 1:
            add_team(teams)

        if action == 2:
            show_all_teams(teams)

        if action == 3:
            add_match_result(teams, matches)

        if action == 4:
            show_standing(teams, matches)

        if action == 5:
            show_leading_team(teams, matches)

        if action == 6:
            show_best_attacking_team(teams)

if __name__ == "__main__":
    main()