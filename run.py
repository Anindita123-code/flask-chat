import os
from flask import Flask


app = Flask(__name__)   # initialize our new flask application


@app.route('/')
def index():
    """ main page with instructions """
    return "To send a message type /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    return "Hi {}" .format(username)


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}" .format(username, message)

    
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
