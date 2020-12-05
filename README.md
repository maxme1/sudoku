This library contains a fast sudoku solver 
that generates all possible solutions to a given puzzle of any shape.

### Usage

```python
from sudoku import solve, print_field

# input as text
puzzle = '''
1 ? 9 ? ? ? 6 ? ?
? ? ? ? ? ? ? ? ?
8 ? ? 4 9 7 ? ? 1
? ? 5 ? ? 2 ? ? ?
? ? 6 7 ? ? ? 1 ?
? ? 1 ? ? ? ? ? 7
7 ? ? 9 4 6 ? ? 2
? 1 ? ? ? ? ? ? ?
? ? 3 ? 7 1 9 ? 8
'''

# the solution is a simple numpy array
solution = next(solve(puzzle))
print_field(solution)
# outputs 
# -------------------------
# | 1 3 9 | 2 8 5 | 6 7 4 |
# | 5 4 7 | 1 6 3 | 2 8 9 |
# | 8 6 2 | 4 9 7 | 3 5 1 |
# -------------------------
# | 3 7 5 | 8 1 2 | 4 9 6 |
# | 2 9 6 | 7 5 4 | 8 1 3 |
# | 4 8 1 | 6 3 9 | 5 2 7 |
# -------------------------
# | 7 5 8 | 9 4 6 | 1 3 2 |
# | 9 1 4 | 3 2 8 | 7 6 5 |
# | 6 2 3 | 5 7 1 | 9 4 8 |
# -------------------------
```
The input can be a numpy array, check `solve`'s docstring for details.
 
There is also a handy shortcut for solving and printing the solutions: 
```python
from sudoku import print_solutions

print_solutions(puzzle, max_solutions=2)

# outputs 
# -------------------------
# | 1 3 9 | 2 8 5 | 6 7 4 |
# | 5 4 7 | 1 6 3 | 2 8 9 |
# | 8 6 2 | 4 9 7 | 3 5 1 |
# -------------------------
# | 3 7 5 | 8 1 2 | 4 9 6 |
# | 2 9 6 | 7 5 4 | 8 1 3 |
# | 4 8 1 | 6 3 9 | 5 2 7 |
# -------------------------
# | 7 5 8 | 9 4 6 | 1 3 2 |
# | 9 1 4 | 3 2 8 | 7 6 5 |
# | 6 2 3 | 5 7 1 | 9 4 8 |
# -------------------------
# 
# -------------------------
# | 1 3 9 | 2 8 5 | 6 7 4 |
# | 5 4 7 | 1 6 3 | 8 2 9 |
# | 8 6 2 | 4 9 7 | 3 5 1 |
# -------------------------
# | 3 7 5 | 8 1 2 | 4 9 6 |
# | 4 8 6 | 7 5 9 | 2 1 3 |
# | 2 9 1 | 6 3 4 | 5 8 7 |
# -------------------------
# | 7 5 8 | 9 4 6 | 1 3 2 |
# | 9 1 4 | 3 2 8 | 7 6 5 |
# | 6 2 3 | 5 7 1 | 9 4 8 |
# -------------------------
```
