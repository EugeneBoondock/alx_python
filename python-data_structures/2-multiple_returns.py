#!/usr/bin/python3

def multiple_returns(sentence):
    result = str(sentence)
    for length in result:
        length = len(result)
        first = result[0]
        return length, first
