import asyncio
import websockets
import json

print("Starting server...")  # Add this to check if the script starts

# Initialize the chess board
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

def move_piece(board, piece, start_row, start_col, end_row, end_col):
    return True

async def handle_client(websocket, path):
    print("Client connected")  # Add this to check client connection
    board = initialize_board()
    await websocket.send(json.dumps({"board": board}))

    async for message in websocket:
        print(f"Received message: {message}")  # Print received message
        data = json.loads(message)
        piece = data.get("piece")
        start_row, start_col = data.get("start")
        end_row, end_col = data.get("end")

        if move_piece(board, piece, start_row, start_col, end_row, end_col):
            await websocket.send(json.dumps({"board": board, "status": "Move successful"}))
        else:
            await websocket.send(json.dumps({"status": "Invalid move"}))

start_server = websockets.serve(handle_client, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
