"""
Codewars Coding Challenge 

Day 89/366

Level 8Kyu Python

Thinkful - Dictionary drills: Order filler

You're running an online business and a big part of your day is fulfilling orders. As your volume picks up that's been taking more of your time, and unfortunately lately you've been running into situations where you take an order but can't fulfill it.

You've decided to write a function fillable() that takes three arguments: a dictionary stock representing all the merchandise you have in stock, a string merch representing the thing your customer wants to buy, and an integer n representing the number of units of merch they would like to buy. Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should return False.

Valid data will always be passed in and n will always be >= 1.

def fillable(stock, merch, n):
    # Your code goes here.


https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python

"""


# My Solutions
def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n



# Test Cases
stock = {"Apple":5, "Banana":10, "Orange":3}
print(fillable(stock, "Apple", 2)) # Output: True (Anda memiliki cukup apel di stok)
print(fillable(stock, "Banana", 15)) # Output: False (Anda tidak memiliki cukup pisang di stok)
print(fillable(stock, "Orange", 5)) # Output: False (Anda tidak memiliki cukup orange di stok)