#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("{} / {} = None".format(a, b))
    finally:
        print("Inside result: {}".format(result))
        print("{} / {} = {}".format(a, b, result))
