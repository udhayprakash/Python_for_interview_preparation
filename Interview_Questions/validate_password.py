"""
Problem:
    Should be between 8 to 10 characters long.
    Should have at least one number.
    Should have at least one uppercase and one lowercase character.
    Should have at least one special symbol.
"""
import re


def validate_string(givenstr):
    if (
        8 <= len(givenstr) <= 10
        and re.search(r"\d", givenstr)
        and re.search("[a-z]", givenstr)
        and re.search("[A-Z]", givenstr)
        and re.search("[@$!%*#?&]", givenstr)
    ):
        return True
    return False


assert validate_string("aA@45678") is True
assert validate_string("aA@4567890") is True
assert validate_string("aA@4567890-") is False
