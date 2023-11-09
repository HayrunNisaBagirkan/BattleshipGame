import random

# Board class
class Board:
    def __init__(self, size, ship_sizes):
        self.size = size  # The size of the game board (10*10).
        self.ship_sizes = ship_sizes  # A dictionary of ship names and their sizes.
        self.guesses = []  # List to store made guesses.
        self.ships = []  # List to store ship locations and types.

    # Populates the boards with player's ships
    def populate_board(self):
        for ship, size in self.ship_sizes.items():
            while True:
                is_vertical = random.choice([True, False])
                if is_vertical:
                    ship_coords = (
                        random.randint(0, self.size - size),
                        random.randint(0, self.size - 1),
                    )
                else:
                    ship_coords = (
                        random.randint(0, self.size - 1),
                        random.randint(0, self.size - size),
                    )
                if not self.has_overlap(ship_coords, size, is_vertical):
                    self.place_ship(ship, ship_coords, size, is_vertical)
                    break

    # Check if ships overlap
    def has_overlap(self, ship_coords, size, is_vertical):
        if is_vertical:
            for i in range(size):
                if (ship_coords[0] + i, ship_coords[1]) in self.ships:
                    return True
        else:
            for i in range(size):
                if (ship_coords[0], ship_coords[1] + i) in self.ships:
                    return True
        return False

    # Places a ship on the board
    def place_ship(self, ship, ship_coords, size, is_vertical):
        if is_vertical:
            for i in range(size):
                self.ships.append((ship_coords[0] + i, ship_coords[1]))
        else:
            for i in range(size):
                self.ships.append((ship_coords[0], ship_coords[1] + i))

    # Player makes a guess
    def make_guess(self):
        while True:
            try:
                row = int(input(f"Make a guess (row 0-{self.size - 1}): "))
                col = int(input(f"Make a guess (column 0-{self.size - 1}): "))
                if 0 <= row < self.size and 0 <= col < self.size:
                    guess = (row, col)
                    if guess in self.guesses:
                        print("You've already guessed this position. Try again.")
                    else:
                        self.guesses.append(guess)
                        return guess
                else:
                    print(f"Please enter valid coordinates (0-{self.size - 1}).")
            except ValueError:
                print(f"Please enter numbers for row and column (0-{self.size - 1}).")

    # Result of an attack on the board
    def mark_board(self, guess, opponent_board, player_name):
        if guess in opponent_board.ships:
            ship = opponent_board.ships[guess]
            print(f"Hit! {player_name} guessed {guess} and hit the {ship}")
            return "*"
        else:
            print(f"Miss! {player_name} guessed {guess}")
            return "X"

# Function for player to set up their own ships
def player_setup(player_name):
    # The size of the game board is set to 10x10.
    size = 10
    # Dictionary of ship names and sizes.
    ship_sizes = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    player_board = Board(size, ship_sizes)

    # Player sets up their own ships manually.
    print(f"{player_name}, it's time to place your ships!")
    player_board.populate_board()

    return player_board

# Function to set up computer's ships randomly
def computer_setup():
    # The size of the game board is set to 10x10.
    size = 10
    # Dictionary of ship names and sizes.
    ship_sizes = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    computer_board = Board(size, ship_sizes)

    computer_board.populate_board()

    return computer_board

# Main function of the game
def play_game(player_name):
    player_board = player_setup(player_name)
    computer_board = computer_setup()

    player_score = 0
    computer_score = 0

    for _ in range(sum(player_board.ship_sizes.values())):
        player_guess = player_board.make_guess()
        computer_guess = (
            random.randint(0, player_board.size - 1),
            random.randint(0, player_board.size - 1)
            )

        player_result = player_board.mark_board(computer_guess, computer_board, player_name)
        computer_result = computer_board.mark_board(player_guess, player_board, "Computer")

        if player_result == "*" and computer_result == "*":
            player_score += 1
            computer_score += 1

    print(f"{player_name}'s Score: {player_score}")
    print(f"Computer's Score: {computer_score}")

# Start a new game
def new_game(player_name):
    while True:
        play_game(player_name)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    print("Welcome!")
    print("Want to see how strong your predictions are?")
    print("Come on and try yourself against the computer.")
    # Prompting the player to enter their name.
    player_name = input("Enter your name: ")
    input("Press Enter to start...")

    new_game(player_name)
