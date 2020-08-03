# BY Alon Galperin

import sys
from flask import Flask,request
from Utils import validations_utils
from Utils import utils

app = Flask("main")

# Add dictionary data structure to app for storing messages in RAM memory
global_messages = {}

#################### Messages Routes ####################

@app.route("/messages", methods=["POST"])
def add_message():
    sender = request.headers.get('messages-user')
    new_message = request.get_json(force=True)
    
    errors = validations_utils.validate_message(new_message)
    if len(errors) > 0:
        return str(errors)

    id = utils.generate_id()
    new_message['sender'] = sender
    new_message['id'] = id
    new_message['date'] = utils.get_current_date_as_string()
    new_message['is_read'] = False

    global_messages[id] = new_message
    return str({"data": global_messages})

@app.route("/messages/<message_id>/read", methods=["PATCH"]) # todo: change to patch method
def read_message_by_id(message_id):
    message = global_messages.get(message_id)
    if message is None:
        return str(f"Message with id {message_id} not found")
    message["is_read"] = True
    return str({"data": message})

@app.route("/messages/<message_id>", methods=["DELETE"]) # todo: change to patch method
def delete_message(message_id):
    requesting_user = request.headers.get('messages-user')
    message = global_messages.get(message_id)
    if message is None:
        return str({"error": "Message did not found"})
    if message["sender"] != requesting_user and message["receiver"] != requesting_user:
        return str({"error": "Only message sender or receiver can delete messages"})
    del global_messages[message_id]
    return str({})

################# End Messages Routes ###################


###################### Uers Routes ######################

@app.route("/users/<username>/messages", methods=["GET"])
def fetch_all_messages_by_user(username):
    filtered_messages = utils.filter_messages_by_username(messages, username)
    return str({"data": filtered_messages})

@app.route("/users/<username>/messages/unread", methods=["GET"])
def get_unread_messages_by_user(username):
    user_messages = utils.filter_messages_by_username(global_messages, username)
    unread_messages = list(filter(lambda message: message["is_read"] == False, user_messages))
    return str({"data": unread_messages})

###################### End Uers Routes #################


@app.route("/")
def hello():
    return str({"data": "Hello World!"})

if __name__ == '__main__':
    if (len(sys.argv) > 1 and str(sys.argv[1])) == "debug":
        app.run(debug=True)
    app.run()