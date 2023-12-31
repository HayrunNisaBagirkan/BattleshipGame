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
    Set the board size, number of ships, player's name,
    the board type (player and computer)
    """
    def __init__(self, size, num_ships, name, type1):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type1
        self.guesses = []
        self.ships = []


    """
    Print the current state of the game board. (print method)
    """
    def print(self):
        for row in self.board:
            print(" ".join(row))


    """
    Set the method for player's guess and update the boards responses.
    (guesses method)
    """
    def add_guesses(self, x, y):
        """
        Parameters:
        -x (int): The row coordinates of the guess.
        -y (int): The column coordinates of the guess.
        Returns:
        - str: If the guess hits a ship returs "Hit", otherwise "Miss".
        """
        self.guesses.append((x, y))
        self.board[x][y] = "x"


        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"


    """
    Add ship to the game board. (add_ship)
    """
    def add_ship(self, x, y):
        """
        Parameters:
        - x (int): The row coordinates to place the ship.
        - y (int): The column coordinates to place the ship.
        - type (str): The type of the ships owner
        """
        self.ships.append((x, y))
        if self.type == "player":
            self.board[x][y] = "o"


"""
Define the 'random_point' function.
"""


def random_point(size):
    """
    Parameters:
    - size (int): The limit for the random integer.
    Returns:
    -int: A random integer in the range [0, size].
    """
    return randint(0, size - 1)


"""
Define the 'valid_coordinates'function.
"""


def valid_coordinates(x, y, size):
    """
    Parameters:
    - x (int): The row coordinates to check.
    - y (int): The column coordinates to check.
    - board (Board): The game board object to check against.
    Returns:
    - bool: If the coordinates are valid, return 'True', otherwise 'False'.
    """
    return 0 <= x < size and 0 <= y < size


"""
Define the 'populate_board' function.
"""


def populate_board(board):
    """
    Parameters:
    -board (Boards): The game board object yo populate with ships.
    """
    for _ in range(board.num_ships):
        while True:
            x = random_point(board.size-1)
            y = random_point(board.size-1)
            if (x, y) not in board.ships:
                board.add_ship(x, y)
                break


"""
Set 'make_guess' and 'play_game' functions for players.
Set maximum number of invalid input.
"""


def make_guess(board):
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        try:
            x = int(input("Enter a number for row (0-5)"))
            y = int(input("Enter a number for column (0-5)"))
            if not valid_coordinates(x, y, board.size):
                print("Invalid coordinates. Please try again!")
            elif (x, y) in board.guesses:
                print("You can not repeat the same choice. Please try again!")
            else:
                result = board.add_guesses(x, y)
                if result == "Hit":
                    print("Player Hit!")
                    scores["player"] += 1
                else:
                    print("Player Missed!")
                break
        except ValueError:
            print("Invalid input. Please enter valid coordinates as integers.")
            attempts += 1

    if attempts == max_attempts:
        print(
            f"You have made {max_attempts} invalid input attempts.GAME OVER"
        )


def play_game(computer_board, player_board):
    while True:
        print("Player's turn")
        print("Player's board")
        player_board.print()
        print("Computer's board")
        computer_board.print()
        make_guess(computer_board)

        if all(
            coord in computer_board.guesses
            for coord in computer_board.ships
        ):
            print(
                f"Player's score: {scores['player']}, "
                f"Computer's score: {scores['computer']}"
            )
            print(f"GAME OVER. {player_board.name} is the WINNER")
            while True:
                play_again = input("Do you want to play again? (Y/N): ")
                if play_again.upper() == "Y":
                    new_game()
                    break
                elif play_again.upper() == "N":
                    print("Thank you! See you next time!")
                    break
                else:
                    print("Invalid input.Please enter'Y'for Yes or'N'for No.")
            break
        print("Computer's Turn")
        x, y = random_point(
            computer_board.size), random_point(computer_board.size)
        result = player_board.add_guesses(x, y)
        if result == "Hit":
            print("Computer Hit!")
            scores["computer"] += 1
            print(
                f"Player's score: {scores['player']}, "
                f"Computer's score: {scores['computer']}"
            )
            print("=" * 40)
        else:
            print("Computer Missed!")
            print(
                f"Player's score: {scores['player']}, "
                f"Computer's score: {scores['computer']}"
            )
            print("=" * 40)

        if all(coord in player_board.guesses for coord in player_board.ships):
            print(
                f"Player's score: {scores['player']}, "
                f"Computer's score: {scores['computer']}"
            )
            print("GAME OVER. Computer is the WINNER")
            while True:
                play_again = input("Do you want to play again? (Y/N): ")
                if play_again.upper() == "Y":
                    new_game()
                    break
                elif play_again.upper() == "N":
                    print("Thank you! See you next time!")
                    break
                else:
                    print("Invalid input.Please enter'Y'for Yes or'N'for No.")
            break


"""
Start a new game with 'new_game' function.
Sets a new game, initializes the board size, number of ships, and player names.
Creates a new game boards and score boards.
"""


def new_game():
    size = 6
    num_ships = 10
    scores["computer"] = 0
    scores["player"] = 0
    print("=" * 40)
    print("Welcome to Battleships Game!")

    print("Want to see how strong your predistions are?")
    print("Come on and try yourself against the computer.")
    print("=" * 40)
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")

    while True:
        print("=" * 40)
        player_name = input("Please enter your name: ")
        if player_name:
            break
        else:
            print("Please enter a valid name!")

    computer_board = Board(size, num_ships, "Computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")
    populate_board(player_board)
    populate_board(computer_board)
    print("=" * 40)

    input("Press ENTER to START the game")
    print("=" * 40)
    play_game(computer_board, player_board)


new_game()

