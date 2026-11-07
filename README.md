# Tic Tac Toe

A simple command-line Tic Tac Toe game for two players (X and O).

## How to run

From this folder:

```bash
python3 tic_tac_toe.py
```

## Players

- X always starts
- Turns switch automatically after each valid move

## Board positions

The board uses positions `0` through `8`:

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

## Commands

| Command | What it does |
|---|---|
| `play <position>` | Place the current player's mark (example: `play 4`) |
| `new` | Reset the board and start a new game (X goes first) |
| `quit` or `exit` | End the program |

## Rules / behavior

- Invalid positions (outside 0-8) are rejected and the turn does not switch
- Taken spots are rejected and the turn does not switch
- After every valid move, the game checks for a winner
- Winning lines: 3 rows, 3 columns, and 2 diagonals

## Functions

- `play(position)` — place a mark, switch turns, check for a winner
- `check_for_winner()` — detect if X or O has won
- `new_game()` — clear the board and reset to X
- `print_board()` — display the board in a 3x3 layout