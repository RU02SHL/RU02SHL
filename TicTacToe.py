# TicTacToe board
board = [[" " for _ in range(3)] for _ in range(3)]
CurrentPlayer = "X"
winner = None

# Scoreboard
Scoreboard = {"X": 0, "O": 0, "Tie": 0}

# Display TicTacToe board
# Can't find a way to get rid of the extra line without disrupting the whole code
def PrintBoard():
    for row in board:
        for spaces in row:
            print(spaces,end = " | ")
        print("\n" + "---------")

# Check if current player has won
def CheckWinner(player):
    for row in board:
        if all(spaces == player for spaces in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if tie
def Full():
    for row in board:
        if " " in row:
            return False
    return True

print("Welcome to TicTacToe!")
print("In this game, you and your friend will take turnsplacing counters on the grid.")
print("To win you need to make 3 in a row")
print("Enjoy !\n")

# Main game loop
while True:
    # Reset board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    while not winner:
        PrintBoard()
        ValidMove = False
        while not ValidMove:
            try:
                move = int(input(f"Player {CurrentPlayer}, enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if 0 <= move <= 8 and board[row][col] == " ":
                    board[row][col] = CurrentPlayer
                    ValidMove = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

        if CheckWinner(CurrentPlayer):
            PrintBoard()
            winner = CurrentPlayer
            print(f"Player {CurrentPlayer} wins!")
            Scoreboard[CurrentPlayer] += 1

        if Full() and not winner:
            PrintBoard()
            print("It's a tie!")
            Scoreboard["Tie"] += 1

        CurrentPlayer = "O" if CurrentPlayer == "X" else "X"

    # Display current Scoreboard
    print(f"Scoreboard - X: {Scoreboard['X']} | O: {Scoreboard['O']} | Tie: {Scoreboard['Tie']}")

    # Ask if the players want to play another game
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != "y":
        break
    winner = None

print("\nThank You for playing \u2764\uFE0F")