# Initialize variables to keep track of points and goal difference.
pointsGained = 0
goalDiff = 0

# Lists representing the number of goals scored and conceded in 11 matches.
goalsFor = [1, 3, 3, 0, 2, 1, 4, 3, 2, 3, 0]
goalsAgainst = [1, 3, 2, 1, 0, 2, 2, 1, 3, 1, 2]

# Loop through each match (11 in total).
for j in range(11):
    # Check if your team scored more goals than the opponent.
    if goalsFor[j] > goalsAgainst[j]:
        # Your team won, so add 3 points to the pointsGained.
        pointsGained += 3
        # Calculate the goal difference and add it to goalDiff.
        goalDiff += (goalsFor[j] - goalsAgainst[j])
    # Check if the match ended in a draw.
    elif goalsFor[j] == goalsAgainst[j]:
        # It's a draw, so add 1 point to the pointsGained.
        pointsGained += 1
    else:
        # Your team lost, so subtract the goal difference from goalDiff.
        goalDiff += (goalsFor[j] - goalsAgainst[j])

# Print the total points and goal difference.
print("Points:", pointsGained)
print("Goal Difference:", goalDiff)
print("===============================================")

# Define a function to create a soccer-related tweet.
def newTweet(player, action, success):
    # Initialize the tweet string with player and action.
    tweet = player + " plays a " + action + " "
    # Check if the action was successful.
    if success:
        # Depending on the action, complete the tweet.
        if action == "pass":
            tweet += "and the team keeps possession."
        elif action == "shot":
            tweet += "and it's a GOAL!"
    else:
        # If the action was not successful, mention it.
        if action == "pass":
            tweet += "but the pass is unsuccessful."
    # Return the constructed tweet.
    return tweet

# Call the newTweet function with player="Grizeman", action="shot", and success=True.
tweet_text = newTweet("Grizeman", "shot", True)
# Print the generated tweet.
print(tweet_text)
