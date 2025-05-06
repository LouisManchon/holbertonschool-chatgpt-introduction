def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if there is a winner.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    """
    Run the main Tic-Tac-Toe game loop.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0

    while not check_winner(board) and moves < 9:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of range. Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        moves += 1

        if check_winner(board):
            break

        player = "O" if player == "X" else "X"

    print_board(board)
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()

