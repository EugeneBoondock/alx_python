#!/usr/bin/python3

def convert_to_celsius(fahrenheit):
    celcius = (5/9) * (fahrenheit - 32)
    if celcius < 0:
        return ("{:2f}".format(celcius))
    else:
        return celcius
