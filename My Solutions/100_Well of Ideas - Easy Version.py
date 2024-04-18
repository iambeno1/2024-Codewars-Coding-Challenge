"""
Codewars Coding Challenge 

Day 100/366

Level 8kyu

Well of Ideas - Easy Version

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.


def well(x):
    #your code here
    return ''

https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python
"""

# Solution
def well(x):
    count_good = x.count("good")

    if count_good == 0:
        return 'Fail!'
    elif count_good <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'

