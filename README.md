# Tournament Project

A terminal app for managing a football tournament. You add teams, enter match results, and the app keeps track of points, standings and stats.

## What it can do?

- Add teams and list them
- Record match results (each pair of teams plays only once)
- Show the standings table, sorted by points, goal difference, goals scored and name
- Show the leading team and the best attacking team
- Show a team's success rate
- Show teams that haven't won yet
- Show a tournament summary
- Check if a team can still win the championship

## How to run?

```bash
python3 main.py
```

Pick an option from the menu, and enter `0` to exit.

To run a demo with sample input:

```bash
python3 main.py < inputs.txt
```

Teams and matches are saved in the `data/` folder.