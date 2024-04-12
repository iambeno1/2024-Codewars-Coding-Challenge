"""
Codewars Coding Challenge

Day 101/366

Level 7kyu

Simple letter removal

In this Kata, you will be given a lower case string and your task will be to remove k characters from that string using the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.
For example: 
solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
solve('abracadabra', 8) = 'rdr'
solve('abracadabra',50) = ''
More examples in the test cases. Good luck!

Please also try:

Simple time difference

Simple remove duplicates


def solve(st,k): 
    pass


https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python
"""

# Solution
def solve(st, k):
    for char in sorted(set(st)):
        count = st.count(char)
        if k >= count:
            st = st.replace(char, '', count)
            k -= count
        else:
            st = st.replace(char, '', k)
            break
    return st
