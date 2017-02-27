# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

A: Step1. Find the possible twins: We create a copy of the unit and go over it box by box. When we find a box with 2 possible solutions, we check the remainder of the unit to see if we can find a box with same possible solutions. If we find another box with the same possible solutions, we eliminate the 2 boxes from the unit in order to narrow the searchspace, not to get the pair twice, and add the possible solutions to a string called twin_values. Once we have finished this operation, if the twin_values string is empty, we move on to the next unit and apply Step1 again. If not, we move on to Step2.

Step2. Eliminate the possible solutions of the twins from all the other boxes: As the copy of our unit contains only the non-twin boxes, all the values for a twin are in the twin_values string. Then we go through all the remanining boxes in the copy of the unit and eliminate the solutions that appear in the twin_values string, and we move on to the next unit with the same operation.  

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

A: We define diagonal_units and add it into the unitlist. Now all the constraint propagation strategies (Eliminate, only choice, naked twins) that are applied on the unitlist will be used across the diagonals, imposing the one element per unit constraint on it. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
