"""
Name = Thomas Martin
Program = eightpuzzle.py
Date: 9/30/19

"""

import copy
import time


class Puzzle():
    """A sliding-block puzzle."""
    def __init__(self, grid, path=None):
        """Instances differ by their number configurations."""
        if path is None:
            path = []
        self.grid = copy.deepcopy(grid) # No aliasing!
        self.path = path

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end = ' '),
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN
        curr = self.grid
        x = -1
        y = -1
        for i in range(3):
            for j in range(3):
                if curr[i][j] == ' ':
                    x, y = i, j
                    break
        moves = []
        if x + 1 < 3:
            moves.append("S")

        if x - 1 >= 0:
            moves.append("N")

        if y - 1 >= 0:
            moves.append("W")

        if y + 1 < 3:
            moves.append("E")

        return moves

    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        #  YOU FILL THIS IN
        location = self.grid
        x = -1
        y = -1
        b = 0
        for i in range(3):
            for j in range(3):
                if location[i][j] == ' ':
                    x = i
                    y = j

        if move == "E":
            currentPath = self.path + [move]
            b = copy.deepcopy(location)
            b[x][y] = b[x][y + 1]
            b[x][y + 1] = ' '

        if move == "S":
            currentPath = self.path + [move]
            b = copy.deepcopy(location)
            b[x][y] = b[x + 1][y]
            b[x + 1][y] = ' '


        if move == "N":
            currentPath = self.path + [move]
            b = copy.deepcopy(location)
            b[x][y] = b[x - 1][y]
            b[x - 1][y] = ' '

        if move == "W":
            currentPath = self.path + [move]
            b = copy.deepcopy(location)
            b[x][y] = b[x][y - 1]
            b[x][y - 1] = ' '


        return Puzzle(b, currentPath)

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
        h = 0
        for i in range(3):
            for j in range(3):
                if goal.grid[i][j] != ' ':
                    value = goal.grid[i][j]
                    value_i = i
                    value_j = j
                    current_i = 0
                    current_j = 0
                    for x in range(3):
                        for y in range(3):
                            current = self.grid[x][y]
                            if current == value:
                                current_j = y
                                current_i = x

                    h += abs(value_i - current_i) + abs(value_j - current_j)
        return h


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def insert(self, puzzle, h):
        self.queue.append((puzzle, h))

    def exists(self, item):
        return item in (x[1] for x in self.queue)

    def pop(self):
        try:
            x = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] < self.queue[x][1]:
                    x = i
            item = self.queue[x]
            del self.queue[x]
            return item
        except IndexError:
            print()
            exit()

class Agent():
 """Knows how to solve a sliding-block puzzle with A* search."""

 def astar(self, puzzle, goal):
    """Return a list of moves to get the puzzle to match the goal."""
    # YOU FILL THIS IN
    finished = []
    frontier = PriorityQueue()
    frontier.insert(puzzle, puzzle.h(goal))

    while frontier:
        node = frontier.pop()
        if node[0].grid == goal.grid:
            return node[0].path

        finished.append(node[0].grid)
        par = node[0].moves()

        for move in par:
            child = node[0].neighbor(move)

            if child.grid in finished or frontier.exists(child.grid):
                continue

            else:
                finished.append(child.grid)
                frontier.insert(child, child.h(goal))


def main():
 """Create a puzzle, solve it with A*, and console-animate."""

 puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
 puzzle.display()

 agent = Agent()
 goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
 path = agent.astar(puzzle, goal)


 while path:
    move = path.pop(0)
    puzzle = puzzle.neighbor(move)
    time.sleep(1)
    puzzle.display()

if __name__ == '__main__':
    main()