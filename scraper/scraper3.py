
import tweepy

# Twitter API credentials
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets related to "Akash"
search_query = "Akash"
tweet_count = 10  # Number of tweets to retrieve

try:
    # Perform the search
    tweets = api.search_tweets(q=search_query, count=tweet_count)

    # Print the tweets
    for tweet in tweets:
        print(tweet.text)
        print("------------")

except Exception as e:
    print("Error: ", str(e))
