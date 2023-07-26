#!/usr/bin/python3

def no_c(my_string):
    my_string = str(my_string)
    for char in my_string:
        if char == my_string[0]:
            if char == 'c' or char == 'C':
                return("{}".format(my_string[1:]))
        else:
            return my_string
