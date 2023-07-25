#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = int(a/b)
    except ZeroDivisionError:
        a or b == 0
        print("{} / {}= None".format(a, b))
    finally:
        a or b != 0
        print("Inside result: {}".format(float(a/b)))
        print("{} / {} = {}".format(a, b, float(a/b)))
