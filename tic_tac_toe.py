"""
Tic-Tac-Toe Game
A two-player console-based Tic-Tac-Toe game.
"""


def print_board(board):
    print()
    for i in range(3):
        row = " | ".join(board[i * 3:(i + 1) * 3])
        print(row)
        if i < 2:
            print("-" * 9)
    print()


def check_winner(board):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def is_board_full(board):
    return " " not in board


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That position is already taken.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Tic-Tac-Toe ===")
    print("Positions are numbered 1-9, left to right, top to bottom.\n")

    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
