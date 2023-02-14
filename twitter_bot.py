import tweepy
import random

# Twitter Developer Account Credentials

api_key = "api_key"
api_key_secret = "api_secret_key"
access_token = "acess_token"
access_token_secret = "acess_token_secret"

# Authenticating the credentials

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


# Posting a tweet

def post_tweet():
    tweet = input("Write your tweet here: ")
    api.update_status(tweet)
    #print("Your Tweet is posted")
    print("Tweeted: {}".format(tweet))


def add_follower():
    api.create_friendship(screen_name=input("account to be followed:"))
    print("Account Followed.")


def edit_profile():
    api.update_profile(name=input("Enter the name:"))
    api.update_profile(description=input("Enter the description:"))
    api.update_profile(location=input("Enter the location:"))


def get_profile_details():
    user = api.get_user(screen_name="UserName") #username of user whose account details to be viewed
    print("User ID = ", user.id)
    print("User name = ", user.name)
    print("User description = ", user.description)
    print("Followers List:")
    for follower in user.followers():
        print(follower.name, "follows", user.name)

# same as above
# for follower in tweepy.Cursor(api.get_followers).items():
#   print(follower.name)


def liking_timeline_tweets():
    tweets_home = api.home_timeline()
    for tweet in tweets_home:
        if tweet.author.name.lower() != "UserName": #provide username to discard liking self tweets
            if not tweet.favorited:
                print("liking", tweet.id, tweet.author.name)
                api.create_favorite(tweet.id)


def liking_profile_tweets():
    user = api.get_user(screen_name=input("Enter User ID:"))
    tweets_user = api.user_timeline(user_id=user.id)
    for tweet in tweets_user:
        if not tweet.favorited:
            print("liking tweet ID", tweet.id, "of", tweet.author.name)
            api.create_favorite(tweet.id)


def search_tweets():
    search = input("The keyword to search:")
    limit = int(input("Enter the number of tweets:"))
    tweets = tweepy.Cursor(api.search_tweets, search, lang="en").items(limit)
    for tweet in tweets:
        print(tweet.author.name, ":", tweet.text, "\n")


def view_home_timeline():
    tweets = api.home_timeline()
    for tweet in tweets:
        print(str(tweet.id), "-", tweet.text, "\n")


def view_user_timeline():
    s_name = input("Enter the screen name of the user:")
    tweets = api.user_timeline(screen_name=s_name)
    print("Displaying tweets of", s_name, "\n")
    for tweet in tweets:
        print(str(tweet.id), "-", tweet.text, "\n")


def view_timeline():
    tweets = api.user_timeline()
    user = api.get_user(screen_name="UserNAme") #provide a username
    print("Displaying tweets of", user.name, "\n")
    for tweet in tweets:
        print(str(tweet.id), "-", tweet.text, "\n")


def retweet():
    ID = input("Enter the ID of the tweet you want to retweet:")
    api.retweet(ID)
    print("Retweet Completed.")


def post_random_tweet():
    lines = open(file_path).read().splitlines() #replace file_path with ypur own
    return random.choice(lines)

msg = post_random_tweet()

with open(r"D:\hashtag.txt", "r") as file:
    f = file.read()
    words = list(map(str, f.split()))
    tag = random.choice(words)

msg += ' ' + tag
if len(msg) < 160:
    api.update_status(msg)
    print("Tweeted: {}".format(msg))


print("1. Post A Tweet")
print("2. Post A Random Tweet")
print("3. View Home Timeline")
print("4. View A Profile's Timeline")
print("5. View Own Timeline")
print("6. Edit Profile Details")
print("7. View Profile Details")
print("8. Add New Followers")
print("9. Like Timeline Tweets")
print("10.Like Tweets in a Profile")
print("11. Search Tweets")
print("12. Retweet")


choice = int(input("Enter a choice:"))

if choice == 1:
    post_tweet()
elif choice == 2:
    post_random_tweet()
elif choice == 3:
    view_home_timeline()
elif choice == 4:
    view_user_timeline()
elif choice == 5:
    view_timeline()
elif choice == 6:
    edit_profile()
elif choice == 7:
    get_profile_details()
elif choice == 8:
    add_follower()
elif choice == 9:
    liking_timeline_tweets()
elif choice == 10:
    liking_profile_tweets()
elif choice == 11:
    search_tweets()
elif choice == 12:
    retweet()
else:
    print("Wrong input!")

