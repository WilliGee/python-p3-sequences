#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    sequence = []

    if length > 0:
        sequence.append(0)

    if length >= 2:
        sequence.append(1)

        for i in range(2,length):
            sequence.append(sequence[-1] + sequence[-2])

    print(sequence)