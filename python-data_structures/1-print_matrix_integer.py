#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            elem = row[i]
            print("{:d}".format(elem), end=" ")
            if i == len(row) - 1:
                print("{:d}".format(elem), end="")
        print()
