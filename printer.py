def print_title(title):
    print(f"\n*** {title} ***\n")

def print_team_detail(t):
    print(f"{t["id"]}. {t["name"]:<7} {t["played"]} games, {t["points"]} points")

def print_no_teams_yet():
    print("There are no teams yet")

def print_no_matches_yet():
    print("There are no matches yet")