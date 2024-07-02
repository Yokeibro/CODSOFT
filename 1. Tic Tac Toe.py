import numpy as np

def create_board():
    return np.array([[' ' for _ in range(3)] for _ in range(3)])

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -np.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -np.inf, np.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def human_move(board):
    while True:
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        if board[row][col] == ' ':
            board[row][col] = 'X'
            break
        else:
            print("Invalid move. Try again.")

def play_game():
    board = create_board()
    print_board(board)
    while True:
        # Human move
        human_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI move
        move = best_move(board)
        board[move[0]][move[1]] = 'O'
        print_board(board)
        if check_win(board, 'O'):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

play_game()
