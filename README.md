# Human Friendly Sudoku Solver

A sudoku solver based on methodologies more familiar to humans rather than brute force solutions.

Implemented strategies:
- Removing solved numbers in each row from possibilities of remaining unsolved numbers in said row
- Removing solved numbers in each column from possibilities of remaining unsolved numbers in said column
- Removing solved numbers in each 3x3 square from possibilities of remaining unsolved numbers in said 3x3 square
- Checking if only one tile in a 3x3 square contains a certain number