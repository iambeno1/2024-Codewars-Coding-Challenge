"""
Codewars Coding Challenge 

Day 91/366

Level 8kyu Python

Cockroach

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

def cockroach_speed(s):
    return 


https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python
"""

# My Solutions
def cockroach_speed(s):
    return int(s * (100000 / 3600))