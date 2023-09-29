import random

# Goal probabilities for home and away teams
HomexG = [0.21, 0.66, 0.1, 0.14, 0.01]
AwayxG = [0.04, 0.06, 0.01, 0.04, 0.06, 0.12, 0.01, 0.06]

# Function to simulate shots and calculate goals
def shotsTest(shots):
    goals = 0

    for shot in shots:
        if random.random() <= shot:
            goals += 1
    return goals

# Simulate 1000 matches
for j in range(0, 1000):
    HomexG_copy = HomexG.copy()  # Make a copy of the original list
    AwayxG_copy = AwayxG.copy()  # Make a copy of the original list

    HomexG_goals = shotsTest(HomexG_copy)
    AwayxG_goals = shotsTest(AwayxG_copy)

    if HomexG_goals > AwayxG_goals:
        print("Home Wins! {} - {}".format(HomexG_goals, AwayxG_goals))
    elif HomexG_goals < AwayxG_goals:
        print("Away Wins! {} - {}".format(HomexG_goals, AwayxG_goals))
    else:
        print("Share of the points! {} - {}".format(HomexG_goals, AwayxG_goals))
