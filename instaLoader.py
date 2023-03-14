import instaloader
import pandas
import re
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'mngugi7')
print(profile)

print('----------------------------------------------------------')
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'mngugi7')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)

print('---------------------------------------------------------')
# Creating an instance of Instaloader class
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, "mngugi7")
print("Username: ", profile.username)
print("Bio: ", profile.biography)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Emails extracted from the bio:")
print(emails)

bot = instaloader.Instaloader()
bot.login(user="Your_username", passwd="Your_password")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'Your_target_account_insta_handle')

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)

# Storing the results in a CSV file
followers_df.to_csv('followers.csv', index=False)

# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]

# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)

# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)