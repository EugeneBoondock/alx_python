#!/usr/bin/python3

def multiple_returns(sentence):
    result = str(sentence)
    length = len(result)
    first = result[0] if length > 0 else None
    return length, first
