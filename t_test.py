import tweepy

auth = tweepy.OAuth2UserHandler(
    client_id="Jm6fgfKm4GyVG452EjSImTEB0",
    client_secret="XStk62FYvUDJrF6xu4OtK5pbSEaHeoQp0fpJHPNNwD24S5L",
    redirect_uri="http://localhost/callback",
    scope=["tweet.read", "users.read", "offline.access"]
)

# Get the authorization URL and open it in your browser
print("Open this URL to authorize:")
print(auth.get_authorization_url())

# After authorizing, paste the full redirect URL
redirect_url = input("Paste the redirect URL here: ")

# Fetch the access token
access_token = auth.fetch_token(redirect_url)

print(access_token)