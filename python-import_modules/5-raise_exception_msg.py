#!/usr/bin/python3

def raise_exception_msg(message=""):
    message = str(input(""))
    try:
        raise NameError(message)
    except NameError:
        raise
