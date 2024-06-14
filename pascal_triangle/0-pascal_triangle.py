#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
  """
  This function generates a list of lists representing Pascal's Triangle up to level n.

  Args:
      n: An integer representing the desired level of Pascal's Triangle.

  Returns:
      A list of lists containing the elements of Pascal's Triangle for level n.
      An empty list if n is less than or equal to 0.
  """

  if n <= 0:
    return []

  triangle = [[1]]  # Initialize the triangle with the first row (always [1])

  # Iterate for each row from level 2 to n
  for i in range(1, n):
    previous_row = triangle[i-1]  # Access the previous row
    current_row = []
    # Build the current row based on the previous row
    for j in range(i + 1):
      if j == 0 or j == i:
        current_row.append(1)  # First and last elements are always 1
      else:
        element = previous_row[j-1] + previous_row[j]
        current_row.append(element)
    triangle.append(current_row)

  return triangle
