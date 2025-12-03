board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_win(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

player = "X"

while True:
    print_board()
    move = int(input(f"Player {player}, choose a position (0-8): "))

    if board[move] != " ":
        print("Spot taken, try again!")
        continue

    board[move] = player
