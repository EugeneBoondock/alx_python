#!/usr/bin/python3

def is_prime(number):
    prime = number * number
    if number == number and number <= 1:
        return False
    elif number % 2 == 0:
        return False
    elif number % 5 == 0:
        return False
    else:
        return True