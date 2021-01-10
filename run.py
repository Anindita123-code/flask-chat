import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)   # initialize our new flask application
app.secret_key = "mySecretKey"
messages = []


def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime('%H:%M:%S')
    messages_dict = {"timestamp": now, "name": username, "message": message}
    messages.append(messages_dict)


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    """Add and display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", user_name=username,
                           chat_messages=messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
