"""
Name: Thomas Martin
Program 2: BFS - Maze
Date:9/13/19
"""
import time

class Maze():
    """A pathfinding problem."""
    def __init__(self, grid, location, path= None):
        """Instances differ by their current agent locations."""
        if path is None:
            path = []
        self.grid = grid
        self.location = location
        self.path = path

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('O', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        current = self.location
        row = current[0]
        col = current[1]
        answer = []

        if self.grid[row][col + 1] == " ":
            answer.append("E")

        if self.grid[row + 1][col] == " ":
            answer.append("S")

        if self.grid[row - 1][col] == " ":
            answer.append("N")

        if self.grid[row][col - 1] == " ":
            answer.append("W")

        return answer

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        location = self.location
        currentPath = self.path + [move]

        row = location[0]
        col = location[1]
        nextMove = []

        if move == "E":
            nextMove.append(row)
            nextMove.append(col + 1)

        if move == "S":
            nextMove.append(row + 1)
            nextMove.append(col)

        if move == "N":
            nextMove.append(row - 1)
            nextMove.append(col)

        if move == "W":
            nextMove.append(row)
            nextMove.append(col - 1)

        return Maze(self.grid, tuple(nextMove), currentPath)


class Agent:
    """Knows how to find the exit to a maze with BFS."""
    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        frontier = [maze]
        explored = [(1, 1)]
        while frontier:
            node = frontier.pop(0)
            for move in node.moves():
                child = node.neighbor(move)
                if child.location not in explored:
                    explored.append(child.location)
                    if child.location == goal.location:
                        return child.path
                    frontier.append(child)

def main():
    """Create a maze, solve it with BFS, and console-animate."""
    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]
    maze = Maze(grid, (1, 1))
    maze.display()
    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()