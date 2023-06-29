# Tic-Tac-Toe Console Game

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            if check_winner(board, current_player):
                print_board()
                print("Player", current_player, "wins!")
                game_over = True
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()

