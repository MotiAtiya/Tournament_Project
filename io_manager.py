from pathlib import Path
import json
import os

TEAMS_PATH = Path(__file__).parent / "data/teams.json"
MATCHES_PATH = Path(__file__).parent / "data/matches.json"

def dump_data(path, data):
    if not os.path.exists(path):
        open(path, 'a').close()

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_data(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return None

def reset_data():
    dump_data(TEAMS_PATH, [])
    dump_data(MATCHES_PATH, [])
