def validate_message(message):
    errors = []
    sender = message.get("sender")
    receiver = message.get("receiver")
    subject = message.get("subject")
    message_body = message.get("message")

    check_field(errors, receiver, "Receiver")
    check_field(errors, subject, "Subject")
    check_field(errors, message_body, "Message")
    return errors

def check_field(errors, field_text, field_name):
    if field_text is None:
        errors.append(f"{field_name} field is missing")
    elif is_field_empty(field_text):
        errors.append(f"{field_name} field is empty")

def is_field_empty(text):
    return len(text.strip()) == 0