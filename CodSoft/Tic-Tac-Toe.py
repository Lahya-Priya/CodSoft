import math

# Global Variables
board = [' ' for _ in range(9)]  # 3x3 board
human = 'O'  # Human plays 'O'
ai = 'X'     # AI plays 'X'

# Utility to print the board
def print_board(board):
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Function to determine if there is a winner
def check_winner(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if the board is full (for a draw)
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, ai):
        return 1
    elif check_winner(board, human):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = human
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# Get the best move for the AI using Minimax
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = ai

# Get the human player's move
def human_move():
    valid = False
    while not valid:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = human
                valid = True
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human's turn
        human_move()
        print_board(board)
        if check_winner(board, human):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn
        ai_move()
        print("AI has made its move:")
        print_board(board)
        if check_winner(board, ai):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
