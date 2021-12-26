import tweepy
import os

def connect_to_twitter():
  # Authenticate to Twitter
  consumer_key = os.environ['API_KEY']
  consumer_secret = os.environ['API_KEY_SECRET']
  access_token = os.environ['ACCESS_TOKEN']
  access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # Create API object
  api = tweepy.API(auth)

  try:
    api.verify_credentials()
    print("Authentication OK")
  except:
    print("Error during authentication")

  # Create a tweet
  #api.update_status("Hello Tweepy")