# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:37:17 2025

@author: malth
"""

def greet(name):
    print(f"Hello, {name}!")


def goldilocks(bed_length):
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")


def square_list(numbers):
    return [num ** 2 for num in numbers]


def fibonacci_stop(max_value):
    fib_sequence = [1, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= max_value:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def clean_pitch(measurements, status_signals):
    cleaned = []
    for pitch, status in zip(measurements, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned.append(-999)
        else:
            cleaned.append(pitch)
    return cleaned