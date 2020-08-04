# BY Alon Galperin

import sys
from flask import Flask,request
from Utils import validations_utils
from Utils import utils

app = Flask(__name__)

# Add dictionary data structure to app for storing messages in RAM memory
global_messages = {}

#################### Messages Routes ####################

@app.route("/api/v1/messages", methods=["POST"])
def add_message():
    sender = request.headers.get('messages-user')
    new_message = request.get_json(force=True)
    new_message["sender"] = sender
    
    errors = validations_utils.validate_message(new_message)
    if len(errors) > 0:
        return str({"error": errors}), 400

    id = utils.generate_id()
    new_message['id'] = id
    new_message['date'] = utils.get_current_date_as_string()
    new_message['is_read'] = False
    new_message['deleted_for_sender'] = False
    new_message['deleted_for_receiver'] = False

    global_messages[id] = new_message
    return str({"data": global_messages}), 201

@app.route("/api/v1/messages/<message_id>/read", methods=["PATCH"])
def read_message_by_id(message_id):
    message = global_messages.get(message_id)
    if message is None:
        return str(f"Message with id {message_id} not found")
    message["is_read"] = True
    return str({"data": message})

@app.route("/api/v1/messages/<message_id>", methods=["DELETE"])
def delete_message(message_id):
    requesting_user = request.headers.get('messages-user')
    message = global_messages.get(message_id)
    if message is None:
        return str({"error": "Message did not found"}), 404
    if message["sender"] != requesting_user and message["receiver"] != requesting_user:
        return str({"error": "Only message sender or receiver can delete messages"}), 403
    if requesting_user == message["sender"]:
        message["deleted_for_sender"] = True
    if requesting_user == message["receiver"]:
        message["deleted_for_receiver"] = True 
    return str({})

################# End Messages Routes ###################


###################### Uers Routes ######################

@app.route("/api/v1/users/<username>/messages", methods=["GET"])
def fetch_all_messages_by_user(username):
    filtered_by_receiver = utils.filter_messages_by_receiver_username(global_messages, username)
    marked_deleted = utils.mark_deleted_messages_for_username(filtered_by_receiver, username)
    return str({"data": marked_deleted})

@app.route("/api/v1/users/<username>/messages/unread", methods=["GET"])
def get_unread_messages_by_user(username):
    user_messages = utils.filter_messages_by_receiver_username(global_messages, username)
    unread_messages = list(filter(lambda message: message["is_read"] == False, user_messages))
    marked_deleted = utils.mark_deleted_messages_for_username(filtered_messages, username)
    return str({"data": marked_deleted})

###################### End Uers Routes #################

@app.route("/api/v1")
def hello():
    return str({"data": "Hello World!"})

if __name__ == '__main__':
    if (len(sys.argv) > 1 and str(sys.argv[1])) == "debug":
        app.run(debug=True)
    app.run()