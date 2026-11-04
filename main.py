from menu import get_action
from teams_manager import add_team, show_all_teams
from matches_manager import add_match_result
from statistics_manager import show_standing, show_leading_team, show_best_attacking_team, show_team_success_rate, show_teams_without_wins, show_tournament_summary, check_championship_potential
import logging
from io_manager import reset_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

ACTIONS = {
    1:  add_team,
    2:  show_all_teams,
    3:  add_match_result,
    4:  show_standing,
    5:  show_leading_team,
    6:  show_best_attacking_team,
    7:  show_team_success_rate,
    8:  show_teams_without_wins,
    9:  show_tournament_summary,
    10: check_championship_potential,
    11: reset_data
    }

def main():
    logging.info("System is up")

    while True:
        action = get_action()
        if action == 0:
            print("bye!")
            return
        ACTIONS[action]()

if __name__ == "__main__":
    main()