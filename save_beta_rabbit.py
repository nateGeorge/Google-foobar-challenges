"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.

Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

# help from:
# http://garethrees.org/2013/06/11/tabular/
# http://codereview.stackexchange.com/questions/91317/google-foobar-challenge-save-beta-rabbit-in-python?newreg=793f3386300e42f6901129a4f412ed51

from functools import wraps

def memoized(table=None):
    """Return a memoizer for functions with a single (hashable) argument.
    The optional argument table gives the initial state of the table
    mapping arguments to results.

    """
    if table is None:
        table = dict()
    def memoizer(f):
        @wraps(f)
        def wrapper(arg):
            try:
                return table[arg]
            except KeyError:
                return table.setdefault(arg, f(arg))
        return wrapper
    return memoizer


def answer(food, grid):
    @memoized({})
    def r((t, i, j)):
        # Smallest remainder from t after subtracting the numbers on a path
        # from top left to (i, j) in grid, or total + 1 if there is no
        # path whose sum is less than or equal to t.
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return food + 1
        elif i == j == 0:
            return t
        else:
            return min(r((t, i - 1, j)), r((t, i, j - 1)))

    remainder = r((food, len(grid) - 1, len(grid) - 1))
    return remainder if remainder <= food else -1

if __name__ == "__main__":
    food = 7
    grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    print answer(food, grid) # should be 0

    food = 12
    grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    print answer(food, grid) # should be 1

    food = 12
    grid = [[0, 2, 5], [11, 11, 11], [2, 3, 3]]
    print answer(food, grid) # should be -1
