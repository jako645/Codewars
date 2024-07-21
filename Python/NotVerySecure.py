import re


def alphanumeric(password):
    return bool(re.match(r'^[a-zA-Z0-9]+$', password))
