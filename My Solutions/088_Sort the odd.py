"""
Codewars Coding Challenge 

Day 88/366

Level 6kyu

Sort the odd

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    pass


https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

"""

# My Solutions
def sort_array(source_array):
    odd_numbers = [num for num in source_array if num % 2 != 0]
    odd_numbers.sort()
    
    result = [num if num % 2 == 0 else odd_numbers.pop(0) for num in source_array]
    return result


# Test Cases:
print(sort_array([7, 1]))  # Output: [1, 7]
print(sort_array([5, 8, 6, 3, 4]))  # Output: [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # Output: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]