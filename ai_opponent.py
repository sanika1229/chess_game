# ai_opponent.py
import random

def get_move(board):
    valid_moves = []

    # Iterate over all pieces to find valid moves
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece.islower():  # Assuming AI plays as black
                for r in range(8):
                    for c in range(8):
                        if board.is_valid_move(row, col, r, c):
                            valid_moves.append((row, col, r, c))

    # Randomly select one of the valid moves
    if valid_moves:
        return random.choice(valid_moves)
    else:
        # If no valid moves are found (which might indicate checkmate or stalemate),
        # just return a move that does nothing
        return (0, 0, 0, 0)
