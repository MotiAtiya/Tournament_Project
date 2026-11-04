from menu import get_action
from teams_manager import add_team, show_all_teams
from matches_manager import add_match_result
from standing import show_standing, show_leading_team, show_best_attacking_team, show_team_success_rate, show_teams_without_wins, show_tournament_summary

def main():
    teams = []
    matches = []

    # ACTIONS = {
    #     1: add_team(teams),
    #     2: show_all_teams(teams),
    #     3: add_match_result(teams, matches),
    #     4: show_standing(teams, matches),
    #     5: show_leading_team(teams, matches),
    #     6: show_best_attacking_team(teams),
    #     7: show_team_success_rate(teams),
    #     8: show_teams_without_wins(teams)
    # }

    while True:
        action = get_action()
        if action == 0:
            print("bye!")
            return

        # ACTIONS[action]

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

        if action == 7:
            show_team_success_rate(teams)

        if action == 8:
            show_teams_without_wins(teams)

        if action == 9:
            show_tournament_summary(teams, matches)


if __name__ == "__main__":
    main()