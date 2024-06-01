# Rainwater Trapping

## Description

This project contains a function to calculate the amount of rainwater that can be trapped between walls after it rains. The walls are represented by a list of non-negative integers where each integer represents the height of a wall with a unit width of 1.

## Function Prototype

```python
def rain(walls)
walls: A list of non-negative integers representing the heights of the walls.
Returns
An integer indicating the total amount of rainwater retained.
Assumptions
The ends of the list (before index 0 and after index walls[-1]) are not walls and will not retain water.
If the list is empty, the function returns 0.
Example Usage
The following is an example of how to use the rain function:

python
Copy code
if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 6
File Structure
0_main.py: Main script to test the rain function.
0-rain.py: Contains the implementation of the rain function.
README.md: This readme file.
How to Run
Clone this repository.
Navigate to the project directory.
Run the main script:
sh
Copy code
./0_main.py
