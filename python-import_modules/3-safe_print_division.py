#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = int(a/b)
    except ZeroDivisionError:
        print("{} / {}= None".format(a, b))
    finally:
        print("Inside result: {}".format(float(a/b)))
        print("{} / {} = {}".format(a, b, float(a/b)))
