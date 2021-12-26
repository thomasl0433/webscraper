# E Sellem Twitter Bot
This project scrapes given URLs to obtain the links for articles, then publishes a tweet when the article count increases.

## Architecture Components
- Web scraper
- Twitter Client
- Web Server
- Uptime Robot

### Web scraper
This python file `main.py` scrapes the provided URL and obtains the link needed for the tweet. It also contains the logic to check for updates in article count

### Twitter Client
This python file `twitter.py` takes the link for the post, makes a caption, and then posts the tweet. This also takes care of twitter specific configuration items.

### Web Server
Since the bot should periodically check the website, it needs to be connected to a web server `keep_alive.py` to be 'woken up' regularly. This will be a Flask app that listens on a certain port, and calls the web scraper upon wake.

### Uptime Robot
This is a free service that pings the replit.com workspace every set amount of time to ensure the program stays up and running.