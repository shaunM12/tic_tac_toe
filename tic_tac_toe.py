board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = "X"

def play(position):
    global current_player

    if position < 0 or position > 8:
        print("Invalid position. Choose 0-8.")
        return
    if board[position] != " ":
        print("Spot already taken. Try again.")
        return
    board[position] = current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    check_for_winner()

def check_for_winner():
    if board[0] == board[1] == board[2] and board[0] != " ":
        print(board[0] + " wins")
    elif board[3] == board[4] == board[5] and board[3] != " ":
        print(board[3] + " wins")
    elif board[6] == board[7] == board[8] and board[6] != " ":
        print(board[6] + " wins")
    elif board[0] == board[3] == board[6] and board[0] != " ":
        print(board[0] + " wins")
    elif board[1] == board[4] == board[7] and board[1] != " ":
        print(board[1] + " wins")
    elif board[2] == board[5] == board[8] and board[2] != " ":
        print(board[2] + " wins")
    elif board[0] == board[4] == board[8] and board[0] != " ":
        print(board[0] + " wins")
    elif board[2] == board[4] == board[6] and board[2] != " ":
        print(board[2] + " wins")

def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def new_game():
    global board, current_player
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"

print_board()

while True:
    command = input("Enter command: ")
    if command == "quit" or command == "exit":
        break
    elif command.startswith("play"):
        parts = command.split()
        position = int(parts[1])
        play(position)
        print_board()
    elif command == "new":
        new_game()
        print_board()
    else:
        print("Unknown command")