# Check if the game is over
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == players[turn]:
            return players[turn]
        if board[0][i] == board[1][i] == board[2][i] == players[turn]:
            return players[turn]
        if board[i][0] == board[1][1] == board[2][2] == players[turn]:
            return players[turn]
        if board[0][2] == board[1][1] == board[2][0] == players[turn]:
            return players[turn]
    return None
# Create the board
board = [[None, None, None],
          [None, None, None],
          [None, None, None]]

# Define the players
players = ["X", "O"]

# Define the turn
turn = 0

# Start the game
while True:

    # Print the board
    print(board)

    # Get the player's move
    row = int(input("enter the row"))
    col = int(input("enter the column"))

    # Check if the move is valid
    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] is not None:
        print("Invalid move")
        continue

    # Make the move
    board[row][col] = players[turn]

    # Check if the game is over
    if check_winner(board) is not None:
        break

    # Switch turns
    turn = (turn + 1) % 2

# Print the winner
winner = check_winner(board)
if winner is not None:
    print(winner + " wins!")
else:
    print("Tie game")
