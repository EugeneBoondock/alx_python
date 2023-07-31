#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_score = None

    for key, value in a_dictionary.items():
        if best_score is None or value > best_score:
            best_key = key
            best_score = value

    return best_key
