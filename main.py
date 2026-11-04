from menu import get_action
from teams_manager import add_team, show_all_teams
from matches_manager import add_match_result
from statistics_manager import show_standing, show_leading_team, show_best_attacking_team, show_team_success_rate, show_teams_without_wins, show_tournament_summary
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    logging.info("System is up")
    
    teams = []
    matches = []

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

if __name__ == "__main__":
    main()