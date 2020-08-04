import uuid
import copy
from datetime import datetime

def filter_messages_by_receiver_username(messages, username):
    filtered_messages = []
    for key in messages:
        message = messages[key]
        if message["receiver"] == username:
            filtered_messages.append(message)
    return filtered_messages

def mark_deleted_messages_for_username(messages, username):
    filtered_messages = []
    for message in messages:
        copy_message = copy.deepcopy(messages)
        is_user_receiver = username == message["receiver"]
        is_user_sender = username == message["sender"]
        if (is_user_receiver and message["deleted_for_receiver"] 
        or 
        is_user_sender and message["deleted_for_sender"]):
                print('filtering: ', message["id"])
                copy_message["subject"] = "deleted message"
                copy_message["message"] = "deleted message"
        filtered_messages.append(copy_message)

def generate_id():
    new_id = uuid.uuid4()
    return str(new_id)[-8:]

def get_current_date_as_string():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")