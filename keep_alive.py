from flask import Flask
from threading import Thread
from replit import db

app = Flask('')
# Hard code in num article var to 50 in database
db["NUM_ARTICLES"] = 50

@app.route('/')
def home():
  return "Cren ✅"

def run():
  # start the web server listening on port 8080
  app.run(host='0.0.0.0',port=8080)

# This will get called in main.py
def keep_alive():
  # make a thread that will diverge and continue running the web server in run()
  t = Thread(target=run)
  t.start()
  # at this point, the main thread from main.py will go back and run the contents of main.py