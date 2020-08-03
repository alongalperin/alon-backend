import uuid
from datetime import datetime

# todo: change to filter by value
def filter_messages_by_username(messages, username):
    filtered_messages = []
    for key in messages: # todo: change to better loop
        message = messages[key] # todo: remove after loop refactor
        if message["receiver"] == username:
            filtered_messages.append(message)
    return filtered_messages


def generate_id():
    new_id = uuid.uuid4()
    return str(new_id)[-8:]

def get_current_date_as_string():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")