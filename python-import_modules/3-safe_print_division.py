#!/usr/bin/python3

def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        try:
            print("Inside result: {}".format(float(a / b)))
        except:
            pass
        return result
