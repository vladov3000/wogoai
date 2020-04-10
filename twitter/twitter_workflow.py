import twitter

#User specifies their own API key
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

def main():

    if (ACCESS_TOKEN_KEY != "" and ACCESS_TOKEN_SECRET != ""):
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)
    else:
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET)

    twitter_ID = input("What is the Twitter ID of your specified user? ")
    twitter_name = input("What is the Twitter Name of the specified user? ")

    users_friends_ID = api.GetFriends(user_id=twitter_ID, screen_name = twitter_name)

    friends = []

    for friend in users_friends_ID:
        friends.append(friend.name)
    
    recent_status = api.GetUserTimeline(count=10, screen_name=twitter_name)

    tweets = []
    
    for tweet in recent_status:
        tweets.append(tweet.full_text)

    #Writes user name, friends list and status list to file
    store_in_file(tweets, friends, twitter_name)


def store_in_file(tweets, friends, twitter_name):
    with open("twitteroutput.txt","w+") as f:
        f.write("User Name: " + twitter_name + "\n")
        f.write("User Friends: " )
    
        for n in friends:
            f.write(n + ", ")
        
        f.write("\n")
    
        f.write("User Status: " + "\n")

        for t in tweets:
            f.write(t + ", ")
        f.close()

if __name__ == "__main__":
    main()
