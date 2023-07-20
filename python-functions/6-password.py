#!/usr/bin/python3

def validate_password(password):
    if len(password) >= 8:
        has_uppercase = False
        has_lowercase = False

        for char in password:
            if char.isspace():
                return False
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True

        return has_uppercase and has_lowercase
    else:
        return False