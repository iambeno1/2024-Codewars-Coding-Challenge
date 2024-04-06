"""
Codewars Coding Challenge 

Day 96/366

Level 8kyu

Up and down, the string grows

Many programming languages provide the functionality of converting a string to uppercase or lowercase. For example, upcase/downcase in Ruby, upper/lower in Python, and toUpperCase/toLowerCase in Java/JavaScript, uppercase/lowercase in Kotlin. Typically, these methods won't change the size of the string.

For example, in Ruby, str.upcase.downcase.size == str.size is true for most cases.

However, in some special cases, the length of the transformed string may be longer than the original. Can you find a string that satisfies this criteria?

For example, in Ruby, That means str.upcase.downcase.size > str.size

You should just set the value of STRANGE_STRING to meet the previous criteria.

Note: Meta programming is not allowed in this kata. So, the size of your solution is limited.



STRANGE_STRING = "foo"


https://www.codewars.com/kata/644b17b56ed5527b09057987/train/python

"""

# My solution
STRANGE_STRING = "ß"
