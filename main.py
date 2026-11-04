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
        match action:
            case 0:
                print("bye!")
                return
            case 1:
                add_team(teams)
            case 2:
                show_all_teams(teams)
            case 3:
                add_match_result(teams, matches)
            case 4:
                show_standing(teams, matches)
            case 5:
                show_leading_team(teams, matches)
            case 6:
                show_best_attacking_team(teams)
            case 7:
                show_team_success_rate(teams)
            case 8:
                show_teams_without_wins(teams)
            case 9:
                show_tournament_summary(teams, matches)

        # ACTIONS[action]

if __name__ == "__main__":
    main()