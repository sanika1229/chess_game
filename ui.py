# ui.py

from chess_board import ChessBoard
from ai_opponent import get_move

def main():
    board = ChessBoard()
    board.display_board()
    move_count = 0

    while move_count < 50:  # Example: stop after 50 moves
        # Get and execute the player's move
        start_pos = input("Enter start position (row,col): ")
        end_pos = input("Enter end position (row,col): ")

        start_row, start_col = map(int, start_pos.split(','))
        end_row, end_col = map(int, end_pos.split(','))

        if board.is_valid_move(start_row, start_col, end_row, end_col):
            board.move_piece(start_row, start_col, end_row, end_col)
        else:
            print("Invalid move. Try again.")
            continue

        board.display_board()

        # AI's turn
        ai_start_row, ai_start_col, ai_end_row, ai_end_col = get_move(board)
        board.move_piece(ai_start_row, ai_start_col, ai_end_row, ai_end_col)
        print(f"AI moved from ({ai_start_row}, {ai_start_col}) to ({ai_end_row}, {ai_end_col})")
        board.display_board()

        move_count += 1

if __name__ == "__main__":
    main()
# ui.py continuation...

def main():
    board = ChessBoard()
    board.display_board()

    while True:
        # Player's turn
        start_pos = input("Enter start position (row,col): ")
        end_pos = input("Enter end position (row,col): ")

        start_row, start_col = map(int, start_pos.split(','))
        end_row, end_col = map(int, end_pos.split(','))

        if board.is_valid_move(start_row, start_col, end_row, end_col):
            board.move_piece(start_row, start_col, end_row, end_col)
        else:
            print("Invalid move. Try again.")

        board.display_board()

        if board.is_checkmate('b'):
            print("Checkmate! You win!")
            break
        elif board.is_stalemate('b'):
            print("Stalemate! It's a draw!")
            break
        elif board.is_in_check('b'):
            print("Check!")

        # AI's turn
        ai_start_row, ai_start_col, ai_end_row, ai_end_col = get_move(board)
        board.move_piece(ai_start_row, ai_start_col, ai_end_row, ai_end_col)
        print(f"AI moved from ({ai_start_row}, {ai_start_col}) to ({ai_end_row}, {ai_end_col})")
        board.display_board()

        if board.is_checkmate('w'):
            print("Checkmate! AI wins!")
            break
        elif board.is_stalemate('w'):
            print("Stalemate! It's a draw!")
            break
        elif board.is_in_check('w'):
            print("Check!")
1