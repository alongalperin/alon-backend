from __main__ import app
from flask import request
from Utils import utils
from Utils import validations_utils

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

    messages = app.config["messages"]
    messages[id] = new_message
    return str(messages)

@app.route("/messages/<message_id>/read", methods=["PATCH"]) # todo: change to patch method
def read_message_by_id(message_id):
    messages = app.config["messages"]
    message = messages.get(message_id)
    if message is None:
        return str(f"Message with id {message_id} not found")
    message["is_read"] = True
    return str(message)


@app.route("/messages/<message_id>", methods=["DELETE"]) # todo: change to patch method
def delete_message(message_id):
    requesting_user = request.headers.get('messages-user')
    messages = app.config["messages"]
    message = messages.get(message_id)
    if message is None:
        return str({"error": "Message did not found"})
    if message["sender"] != requesting_user and message["receiver"] != requesting_user:
        return str({"error": "Only message sender or receiver can delete messages"})
    del messages[message_id]
    return str({})