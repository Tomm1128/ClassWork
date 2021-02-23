"""
Thomas Martin
CSC 481
"""
import copy
import time
import abc
import random


class Game(object):
    """A connect four game."""
    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
            """Return a list of possible moves given the current board."""
            # YOU FILL THIS IN
            possible = []
            curr = self.grid

            if curr[0][0] != 'R' and curr[0][0] != 'B':
                possible.append(0)
            if curr[0][1] != 'R' and curr[0][1] != 'B':
                possible.append(1)
            if curr[0][2] != 'R' and curr[0][2] != 'B':
                possible.append(2)
            if curr[0][3] != 'R' and curr[0][3] != 'B':
                possible.append(3)
            if curr[0][4] != 'R' and curr[0][4] != 'B':
                possible.append(4)
            if curr[0][5] != 'R' and curr[0][5] != 'B':
                possible.append(5)
            if curr[0][6] != 'R' and curr[0][6] != 'B':
                possible.append(6)
            if curr[0][7] != 'R' and curr[0][7] != 'B':
                possible.append(7)

            return possible
    def neighbor(self, col, color):
            """Return a Game instance like this one but with a move made into the specified column."""
            # YOU FILL THIS IN
            location = self.grid
            nextMove = copy.deepcopy(location)
            d = 0
            if col == 0:
                while (d + 1) < 8 and location[d + 1][0] == '-':
                    d = d + 1
                nextMove[d][0] = color
            if col == 1:
                while (d + 1) < 8 and location[d + 1][1] == '-':
                    d = d + 1
                nextMove[d][1] = color
            if col == 2:
                while (d + 1) < 8 and location[d + 1][2] == '-':
                    d = d + 1
                nextMove[d][2] = color
            if col == 3:
                while (d + 1) < 8 and location[d + 1][3] == '-':
                    d = d + 1
                nextMove[d][3] = color
            if col == 4:
                while (d + 1) < 8 and location[d + 1][4] == '-':
                    d = d + 1
                nextMove[d][4] = color
            if col == 5:
                while (d + 1) < 8 and location[d + 1][5] == '-':
                    d = d + 1
                nextMove[d][5] = color
            if col == 6:
                while (d + 1) < 8 and location[d + 1][6] == '-':
                    d = d + 1
                nextMove[d][6] = color
            if col == 7:
                while (d + 1) < 8 and location[d + 1][7] == '-':
                    d = d + 1
                nextMove[d][7] = color
            return Game(nextMove)

    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN
        if self.grid[0][0] == '-':
            if self.grid[4][0] != '-':
                return 0

        if self.grid[0][0] != 'R' and self.grid[0][0] != 'B':
            return 5

        if self.grid[0][5] != 'R' and self.grid[0][5] != 'R':
            return 5

        if self.grid[0][0] != '-' or self.grid[0][1] != '-':
            return 5
        return 5


    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        # YOU FILL THIS IN
        check = 0
        # check horizontal spaces
        for y in range(8):
            for x in range(8 - 3):
                if self.grid[x][y] == 'R' and self.grid[x + 1][y] == 'R' and self.grid[x + 2][y] == 'R' and self.grid[x + 3][y] == 'R':
                    return float("inf")

        for y in range(8):
            for x in range(8 - 3):
                if self.grid[x][y] == 'B' and self.grid[x + 1][y] == 'B' and self.grid[x + 2][y] == 'B' and self.grid[x + 3][y] == 'B':
                    return float("-inf")

        # check vertical spaces
        for x in range(8):
            for y in range(8 - 3):
                if self.grid[x][y] == 'R' and self.grid[x][y + 1] == 'R' and self.grid[x][y + 2] == 'R' and \
                        self.grid[x][y + 3] == 'R':
                    return float("inf")

        for x in range(8):
            for y in range(8 - 3):
                if self.grid[x][y] == 'B' and self.grid[x][y + 1] == 'B' and self.grid[x][y + 2] == 'B' and \
                        self.grid[x][y + 3] == 'B':
                    return float("-inf")

        # check / diagonal spaces
        for x in range(8 - 3):
            for y in range(3, 8):
                if self.grid[x][y] == 'R' and self.grid[x + 1][y - 1] == 'R' and self.grid[x + 2][y - 2] == 'R' and self.grid[x + 3][y - 3] == 'R':
                    return float("inf")

        for x in range(8 - 3):
            for y in range(3, 8):
                if self.grid[x][y] == 'B' and self.grid[x + 1][y - 1] == 'B' and self.grid[x + 2][y - 2] == 'B' and self.grid[x + 3][y - 3] == 'B':
                    return float("-inf")

        # check \ diagonal spaces
        for x in range(8 - 3):
            for y in range(8 - 3):
                if self.grid[x][y] == 'R' and self.grid[x + 1][y + 1] == 'R' and self.grid[x + 2][y + 2] == 'R' and self.grid[x + 3][y + 3] == 'R':
                    return float("inf")

        for x in range(8 - 3):
            for y in range(8 - 3):
                if self.grid[x][y] == 'B' and self.grid[x + 1][y + 1] == 'B' and self.grid[x + 2][y + 2] == 'B' and self.grid[x + 3][y + 3] == 'B':
                    return float("-inf")

        if check > 63:
            print("Board is Full")
            return 1

        return None

class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass

class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # YOU FILL THIS IN
        randomSelection = game.possible_moves()
        move = random.randrange(1, (len(randomSelection)))
        return randomSelection[move - 1]

class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        # YOU FILL THIS IN
        move = game.possible_moves()
        return move[0]

class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        # YOU FILL THIS IN
        d = 3
        return self.min_value(game, d)

    def max_value(self, game, depth):
        d = depth
        value = game.utility()
        posmoves = game.possible_moves()
        if depth == 0 or game.winning_state():
            return posmoves[0]

        random.shuffle(posmoves)
        child = game.neighbor(posmoves[0], self.color)
        value = max(value, self.min_value(child, d - 1))
        return value

    def min_value(self, game, depth):
        d = depth
        value = game.utility()
        posmoves = game.possible_moves()
        if depth == 0 or game.winning_state():
            return posmoves[0]

        random.shuffle(posmoves)
        child = game.neighbor(posmoves[0], self.color)
        value = min(value, self.max_value(child, d - 1))
        return value


def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0
    for i in range(simulations):

        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations

def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = RandomAgent('R')
    #maxplayer = FirstMoveAgent('R')
    #minplayer = RandomAgent('B')
    minplayer = MinimaxAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game

if __name__ == '__main__':
    #single_game(io=True)
    tournament(simulations=500)