"""
Codewars Coding Challenge

Day 93/366

Level 7kyu Python

Powers of i

https://www.codewars.com/kata/5a97387e5ee396e70a00016d/train/python
"""

# My Solution
def pofi(n):
    return '1' if n % 4 == 0 else 'i' if n % 4 == 1 else '-1' if n % 4 == 2 else '-i'
