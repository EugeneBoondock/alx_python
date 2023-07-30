#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = set()
    for x in set_1:
        for y in set_2:
            if x == y:
                common_set.add(x)
    return list(common_set)