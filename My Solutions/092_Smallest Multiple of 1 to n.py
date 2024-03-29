"""
Codewars Coding Challenge 

Day 92/366

Levevl 5Kyu Python

Smallest Multiple of 1 to n

Introduction
It's Christmas (a bit late, I know), and you finally decide to do something nice for once in your life.

As you're going to meet up with your family, you think to give them a little something, and what's a better gift than money? I mean, it's kind of hard to find something that both a geriatric and tiktok child would enjoy.

However, there's a little problem: you don't remember how many people there are in the family anymore. Among so much breeding and unaliving, it's just impossible to keep track of the exact count. Also, who knows if that 8th degree cousin will show up—is that even family anymore?

Well, you're at least sure of one thing. There will be, at max, n people at the gathering (excluding you). God only knows how you came up with that upper bound, but you did.

Now, you must be sure that everyone receives the same amount of money; politics brings about enough discussion already.

Furthermore, no money can be left over; they would notice and call you greedy.

Thus, you decide to bring the smallest amount of one dollar bills, such that no matter how many people show up, within your estimated range, everyone gets the same and no money is left over.

Task
Given a positive integer n, return the smallest possible integer, such that it is a multiple of all numbers from 1 to n, both inclusive.

As the results tend to get very big, return your answer modulus 1_000_000_007, i.e., answer % 1_000_000_007.

Performance
The performance requirements are relatively high for this one, so just taking the lowest common multiple from 1 to n, won't work.

On the random tests:

- Random Tests: 100 tests
- Integer Size: 1 to 3_000_000
Examples
  1  ->            1
  2  ->            2
  6  ->           60
 10  ->        2_520
 20  ->  232_792_560
 81  ->  853_087_536
243  ->  309_031_427



def smallest_multiple(n: int) -> int:
    return 1_000_000_007

https://www.codewars.com/kata/65ad9094c5a34200245f3a8f/train/python
"""

# My Solutions
def fpb(a, b):
    while b:
        a, b = b, a % b
    return a

def kpk(a, b):
    return a * b // fpb(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(2, n + 1):
        result = kpk(result, i)
    return result % 1_000_000_007


# Test Cases
print(smallest_multiple(1))   # Output: 1
print(smallest_multiple(2))   # Output: 2
print(smallest_multiple(6))   # Output: 60
print(smallest_multiple(10))  # Output: 2520
print(smallest_multiple(20))  # Output: 232792560
print(smallest_multiple(81))  # Output: 853087536
print(smallest_multiple(243)) # Output: 309031427
