#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("{} / {} = None".format(a, b))
        result = None
    finally:
        print("Inside result: {}".format(float(a / b)))
        return result
