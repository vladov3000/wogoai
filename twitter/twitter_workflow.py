import twitter

CONSUMER_KEY = "dQXFolLAYrgAkeHeur2avDzbc"
CONSUMER_SECRET = "YK7FN6SNehS9MXfS2tWlrTYSOGt6aI3gUJdqceQzFYq3r6K16q"
ACCESS_TOKEN_KEY = "949893216928645121-UowtQ9XSP5Mn0Ai0RbRBpRNDTAq4aZO"
ACCESS_TOKEN_SECRET = "fU2VZsxJX651cbXoRSEn5e4MJVbYRdhG9S0SYISoJj2Vh"

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

    users_friends = api.GetFriendIDsPaged(user_id=twitter_ID, screen_name = twitter_name)
    print("List of " + twitter_name + " friend's IDs: ")

    print(users_friends)

    
    
if __name__ == "__main__":
    main()
