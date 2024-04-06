"""
Codewars Coding Challenge

Day 98/366

Level 7kyu

Change two-dimensional array

Function receive a two-dimensional square array of random integers. On the main diagonal, all the negative integers must be changed to 0, while the others must be changed to 1 (Note: 0 is considered non-negative, here).

(You can mutate the input if you want, but it is a better practice to not mutate the input)

Example:

Input array

[
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]
]
Output array

[
  [ 0,  4, -5, -9,  3 ],
  [ 6,  0, -7,  4, -5 ],
  [ 3,  5,  1, -9, -1 ],
  [ 1,  5, -7,  0, -9 ],
  [-3,  2,  1, -5,  1 ]
]


https://www.codewars.com/kata/581214d54624a8232100005f/train/python

"""

# Solutions
def matrix1(array): 
    # Create a new array to store the modified values
    result = []
    
    # Iterate over each row of the input array
    for i in range(len(array)):
        row = []
        # Iterate over each element in the current row
        for j in range(len(array[i])):
            # Check if the element is on the main diagonal
            if i == j:
                # Change negative integers to 0, otherwise to 1
                if array[i][j] < 0:
                    row.append(0)
                else:
                    row.append(1)
            else:
                # Keep the original value
                row.append(array[i][j])
        # Append the modified row to the result array
        result.append(row)
    
    return result