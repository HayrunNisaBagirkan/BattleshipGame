# NISA'S BATTLESHIPS GAME

Nisa's Battleship Game is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku. This is a classic strategy game where you, the player, compete against the computer to sink each other's ships. Your goal is to outsmart the computer and destroy all of its ships before it does the same to you. Let the battle begin!

[Here is the live version of my project.](https://game-battleship-game-f47322463f60.herokuapp.com/)

![Am I Responsive](/screenshots/am-I-responsive.png)

## How To Play

The game is played on a 6x6 grid, and each player has 10 ships to strategically position on their board.

The player writes a name and presses enter to start the fun.

Player will enter coordinates to guess where the computer's ships are located.
Rows and columns are numbered from 0 to 5.

The computer will randomly guess coordinates on player's board.
If one of the players guess hits one of opponent's ships, it's a "Hit." Otherwise, it's a "Miss."

The game continues until either player or the computer sinks all of the opponent's ships.
The player with the most points wins. Each "Hit" scores a point.



## Game Flow

![Run Program](/screenshots/1.run_program.png)

### Initialization:

A warm and exciting welcome message greets the player and gives brief information about the game.

![Valid name](/screenshots/2.valid_name.png)
Player need to enter a valid name.

![Start Game](/screenshots/3.start_game.png)
Enter to start the game.

![Game Boards](/screenshots/4.game_boards.png)

The game begins by setting up the board size and the number of ships for each player.

The computer's and player's boards will be displayed.

![Valid coordinates](/screenshots/5.valid_invalid_coordinates.png)

Player will be prompted to enter valid coordinates for guesses.

![Game board and Score](/screenshots/6.game_board_and_score.png)

The computer will make a random guess on player's board.

Both of the player can not choose the same choice.

Scores will be updated based on hits and misses.

![Winner and Play again question](/screenshots/8.winner_and_play_again_question.png)

The game ends when either player or the computer sinks all opponent ships.

The winner is declared, and scores are displayed.

The player is asked if they wants to play again.

![Start again](/screenshots/10.Resart_the_game_with_answer_Y.png)

If Yes game start again.

![Finish the game](/screenshots/11.%20Finish_the_game_with_answer_N.png)

If No displays message.

## Game Features

- Player vs. Computer gameplay
- Dynamic board with ship placement
- User-friendly command-line interface
- Scoring system to track player and computer performance
- Option to play multiple rounds

## Feedback and Support
If you encounter any issues, have suggestions for improvement, or want to contribute to the project, feel free to open an issue or create a pull request.

Enjoy the Battleships Game!

## Testing

![PEP8](/screenshots/PEP8_Python_Validator.png)
Passed the code through a PEP8 inter and confirmed there are no problems.