#!/usr/bin/python3

def convert_to_celsius(fahrenheit):
    celcius = (5/9) * (fahrenheit - 32)
    if fahrenheit < 0 and type(fahrenheit) == float:
        return (f"{celcius:.2f}")
    else:
        return celcius
