"""
Purpose: Validate username problem for

    A username is valid if it satisfies the following rules:
        - username must be atleast 4 characters long.
        - username must contain only letters, numbers and optionally
            one underscore(_).
        - username must start with a letter, and must not end with an
           underscore.  The
"""
import re


def validate(username):
    if not re.match("^[^_]*(_[^_]*){0,1}$", username):
        return False
    pattern = re.match("^(?=.{4,}$)(?![0-9_])[a-zA-Z0-9_]+(?<![_])$", username)
    return True if pattern else False


print(validate("Mike_Standish"))  # Valid username
print(validate("Mike Standish"))  # Invalid username


assert validate("Mik") is False
assert validate("Mike") is True
assert validate("Mike__Standish") is False
assert validate("Mike Standish") is False

assert validate("Mike_Standish") is True
assert validate("Mike__Standish") is False
assert validate("Mike_Standish_") is False
assert validate("Mike_Stand_ish") is False
