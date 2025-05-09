from Board import Board
import random
def parse_move(move_str):
    try:
        start_str, end_str = move_str.strip().split()
        start = (8 - int(start_str[1]), ord(start_str[0]) - ord('a'))
        end = (8 - int(end_str[1]), ord(end_str[0]) - ord('a'))
        return start, end
    except:
        print("Invalid input format. Use e.g. 'e2 e4'")
        return None, None

def index_to_notation(index):
    row, col = index  # Get row and column from the index
    file = chr(ord('a') + col)  # Convert column 0–7 to letters 'a'–'h'
    rank = str(8 - row)         # Convert row 0–7 to ranks '8'–'1'
    return file + rank          # Join file and rank (e.g., 'e2')


def main():
    board = Board()
    turn = "white"

    while True:
        board.show_board()
        if turn == "white":
            print(f"{turn.capitalize()}'s turn")
            move = input("Enter move (e.g. e2 e4): ")
            if move.lower() == "quit":
                break

            start, end = parse_move(move)
            if not start or not end:
                continue

            piece = board.get_piece(start)
            if piece is None:
                print("No piece there.")
                continue

            if piece.color != "white":
                print("That’s not your piece.")
                continue

            moved = board.move_piece(start, end)
            if moved:
                turn = "black"
                    # if turn == "white" else "white"
            # else:
            #     print("Invalid move.")
        else:
            print("Computer’s turn (Black)...")
            import time
            time.sleep(1)  # Pause for effect

            all_moves = board.get_all_valid_moves("black")
            if not all_moves:
                print("Computer has no moves! You win!")
                break

            start, end = random.choice(all_moves)
            board.move_piece(start, end)
            print(f"Computer moved from {index_to_notation(start)} to {index_to_notation(end)}")
            turn = "white"

if __name__ == "__main__":
    main()
