"""
Module and function
"""
from random import randint

"""
Scoreboard
"""
scores = {"computer": 0, "player": 0}

"""
Define Board class
"""
class Board:
"""
Main board class. Sets board size, the number of ships,
the player's name, the board type (player board or computer).
Has methods for adding ships and guesses and printing the board.
"""


"""
Define __init__ method to initialize a new game board.
Set the board size, number of ships, player's name, the board type (player and computer)
"""
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []


"""
Print the current state of the game board. (print method)
"""


"""
Set the method for player's guess and update the boards responses. (guesses method)
"""


"""
Add ship to the game board. (add_ship)
"""


"""
Generate random integer coordinates within the specified board size with 'random_point' function.
"""


"""
Check if given coordinations are valid with 'valid_coordinates'function.
"""


"""
Populate the game board with ships with 'populate_board' function.
"""


"""
Set 'make_guess' and 'play_game' functions for players.
"""


"""
Start a new game with 'new_game' function.
Sets a new game, initializes the board size, number of ships, and player names.
Creates a new game boards and score boards.
"""

