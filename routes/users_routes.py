from __main__ import app
from Utils import utils

@app.route("/users/<username>/messages", methods=["GET"])
def fetch_all_messages_by_user(username):
    messages = app.config["messages"]
    filtered_messages = utils.filter_messages_by_username(messages, username)
    return str(filtered_messages)

@app.route("/users/<username>/messages/unread", methods=["GET"])
def get_unread_messages_by_user(username):
    messages = app.config["messages"]
    user_messages = utils.filter_messages_by_username(messages, username)
    unread_messages = list(filter(lambda message: message["is_read"] == False, user_messages))
    return str(unread_messages)