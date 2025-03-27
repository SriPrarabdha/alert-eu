import snscrape.modules.twitter as sntwitter

def get_tweet_interactions_snscrape(tweet_url):
    """
    Retrieve interactions using snscrape
    Works well for public tweets
    """
    interactions = {
        'likes': [],
        'retweets': [],
        'replies': []
    }
    
    try:
        # Fetch tweet details
        tweet = list(sntwitter.TwitterTweetScraper(tweet_url).get_items())[0]
        
        # Note: Actual user details might be limited
        print(f"Tweet Metrics:")
        print(f"Likes: {tweet.likeCount}")
        print(f"Retweets: {tweet.retweetCount}")
        print(f"Replies: {tweet.replyCount}")
        
        return interactions
    except Exception as e:
        print(f"Error retrieving tweet: {e}")
        return interactions
    
# print(get_tweet_interactions_snscrape("https://x.com/elonmusk/status/1904932756163084676"))

# import tweepy


# bearer_token = "AAAAAAAAAAAAAAAAAAAAAKdIaQEAAAAAxeYDSLjqpYWl6shbycFtKIb%2Falk%3D3AlE1I8W7tgrxo7uSwxN8NM3UPQNZ6xSxPnE8olwXV5LPwucHb"

# client = tweepy.Client(bearer_token)

# tweet_id = 1460323737035677698

# response = client.get_liking_users(tweet_id, user_fields=["profile_image_url"])

# for user in response.data:
#     print(user.username, user.profile_image_url)

# {"API Key":"Jm6fgfKm4GyVG452EjSImTEB0",
# "API Key Secret":"XStk62FYvUDJrF6xu4OtK5pbSEaHeoQp0fpJHPNNwD24S5L",
# "bearer"":"""AAAAAAAAAAAAAAAAAAAAAKdIaQEAAAAAxeYDSLjqpYWl6shbycFtKIb%2Falk%3D3AlE1I8W7tgrxo7uSwxN8NM3UPQNZ6xSxPnE8olwXV5LPwucHb""",
# "Access Token":"1273271202149044226-YtOQIVUTVNI9NWvrGDdATpWwHtG6WU",
# "Access Token Secret":"k8V0ydwDJqCfQefAfzPJ6ji5VX4AGWcpphkw951pi3Ma5"}

import tweepy

# Replace these with your actual Twitter API credentials
consumer_key = "Jm6fgfKm4GyVG452EjSImTEB0"
consumer_secret = "XStk62FYvUDJrF6xu4OtK5pbSEaHeoQp0fpJHPNNwD24S5L"
access_token = "1273271202149044226-YtOQIVUTVNI9NWvrGDdATpWwHtG6WU"
access_token_secret = "k8V0ydwDJqCfQefAfzPJ6ji5VX4AGWcpphkw951pi3Ma5"

# Authenticate with Twitter API
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Specify the tweet ID (replace with the actual tweet ID)
tweet_id = 1905151190872309907

try:
    # Collect all users who liked the tweet
    all_users = []
    for response in tweepy.Paginator(client.get_liking_users, tweet_id):
        if response.data:
            all_users.extend(response.data)
    
    # Check if any users were found and print their usernames
    if all_users:
        print("Users who liked the tweet:")
        for user in all_users:
            print(user.username)
    else:
        print("No likes found for this tweet.")
except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")
