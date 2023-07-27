#!/usr/bin/python3

def multiple_returns(sentence):
    result = str(sentence)
    for leng in result:
        leng = len(result)
        first = result[0]
        return("Length: {:d} - First character: {}".format(leng, first))
