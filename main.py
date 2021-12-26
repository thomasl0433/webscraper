# TO DO:
#  - connect to twitter api
#  - automate script to periodically check for new articles
#  - post tweet when num_articles increases

from keep_alive import keep_alive
import requests
from replit import db
from bs4 import BeautifulSoup
from twitter import connect_to_twitter

URL = "https://www.kfvs12.com/authors/lucas-sellem/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# obtain the container that holds the search results
results = soup.find("section", class_="recommendations")

# obtain an array of each search result
search_results = results.find_all("div", class_="flex-feature")

num_articles = len(search_results)

def check_for_new_article():
  if num_articles > db["NUM_ARTICLES"]:
    db["NUM_ARTICLES"] = num_articles
    return True

def print_num_articles():
  print("Lucas has written " + str(num_articles) + " articles")

def print_articles():
  for item in search_results:
    title = item.find("span")
    link = item.find("a", class_="text-reset")
    print(title.text.strip())
    print("https://www.kfvs12.com" + link['href'])
    print()

# Program execution starts HERE:

# This runs keep_alive() in keep_alive.py, which starts a thread of execution to run this file, and one to run a web server to continiously listen for requests
#keep_alive()

# check if article count increased
#if check_for_new_article() == True:
if True:
  # make Twitter post
  connect_to_twitter()

#print_articles()
#print_num_articles()

# peep twitter.py 
