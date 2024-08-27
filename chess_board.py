def initialize_board():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_valid_position(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def is_empty(board, row, col):
    return board[row][col] == '.'

def move_pawn(board, start_row, start_col, end_row, end_col):
    if not is_valid_position(start_row, start_col) or not is_valid_position(end_row, end_col):
        return False

    piece = board[start_row][start_col]
    if piece.lower() != 'p':
        return False

    direction = -1 if piece == 'P' else 1  # White pawns move up (-1), Black pawns move down (+1)

    # Check if moving vertically
    if start_col == end_col:
        if end_row == start_row + direction and is_empty(board, end_row, end_col):
            board[end_row][end_col] = piece
            board[start_row][start_col] = '.'
            return True
        if (start_row == 1 and piece == 'p' or start_row == 6 and piece == 'P') and end_row == start_row + 2 * direction and is_empty(board, end_row, end_col):
            board[end_row][end_col] = piece
            board[start_row][start_col] = '.'
            return True
    # Check for diagonal capture
    elif abs(start_col - end_col) == 1:
        if end_row == start_row + direction and board[end_row][end_col] != '.' and board[end_row][end_col].islower() if piece.isupper() else board[end_row][end_col].isupper():
            board[end_row][end_col] = piece
            board[start_row][start_col] = '.'
            return True

    return False

def move_rook(board, start_row, start_col, end_row, end_col):
    if not is_valid_position(start_row, start_col) or not is_valid_position(end_row, end_col):
        return False

    piece = board[start_row][start_col]
    if piece.lower() != 'r':
        return False

    # Rook moves horizontally or vertically
    if start_row == end_row or start_col == end_col:
        if is_path_clear(board, start_row, start_col, end_row, end_col):
            if is_empty(board, end_row, end_col) or (board[end_row][end_col].islower() if piece.isupper() else board[end_row][end_col].isupper()):
                board[end_row][end_col] = piece
                board[start_row][start_col] = '.'
                return True
    return False

def is_path_clear(board, start_row, start_col, end_row, end_col):
    if start_row == end_row:
        step = 1 if end_col > start_col else -1
        for col in range(start_col + step, end_col, step):
            if not is_empty(board, start_row, col):
                return False
    elif start_col == end_col:
        step = 1 if end_row > start_row else -1
        for row in range(start_row + step, end_row, step):
            if not is_empty(board, row, start_col):
                return False
    return True

def main():
    board = initialize_board()
    print_board(board)

    while True:
        try:
            start = input("Enter start position (row,col): ").strip()
            end = input("Enter end position (row,col): ").strip()

            start_row, start_col = map(int, start.split(','))
            end_row, end_col = map(int, end.split(','))

            piece = board[start_row][start_col].lower()
            if piece == 'p':
                if move_pawn(board, start_row, start_col, end_row, end_col):
                    print_board(board)
                else:
                    print("Invalid move. Try again.")
            elif piece == 'r':
                if move_rook(board, start_row, start_col, end_row, end_col):
                    print_board(board)
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid piece or movement not implemented yet.")
        except ValueError:
            print("Invalid input. Enter the position as 'row,col' (e.g., 1,2).")
        except IndexError:
            print("Position out of range. Enter positions between 0 and 7.")
def move_piece(board, piece, start_row, start_col, end_row, end_col):
    if piece.lower() == 'p':
        return move_pawn(board, start_row, start_col, end_row, end_col)
    elif piece.lower() == 'r':
        return move_rook(board, start_row, start_col, end_row, end_col)
    else:
        print("Piece type not supported.")
        return False

def main():
    board = initialize_board()
    print_board(board)

    while True:
        try:
            piece = input("Enter piece type (p for pawn, r for rook): ").strip().lower()
            start = input("Enter start position (row,col): ").strip()
            end = input("Enter end position (row,col): ").strip()

            start_row, start_col = map(int, start.split(','))
            end_row, end_col = map(int, end.split(','))

            if move_piece(board, piece, start_row, start_col, end_row, end_col):
                print_board(board)
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter the position as 'row,col' (e.g., 1,2).")
        except IndexError:
            print("Position out of range. Enter positions between 0 and 7.")

if __name__ == "__main__":
    main()
