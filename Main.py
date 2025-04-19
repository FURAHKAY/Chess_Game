from Board import Board

def parse_move(move_str):
    try:
        start_str, end_str = move_str.strip().split()
        start = (8 - int(start_str[1]), ord(start_str[0]) - ord('a'))
        end = (8 - int(end_str[1]), ord(end_str[0]) - ord('a'))
        return start, end
    except:
        print("Invalid input format. Use e.g. 'e2 e4'")
        return None, None

def main():
    board = Board()
    turn = "white"

    while True:
        board.show_board()
        print(f"{turn.capitalize()}'s turn")
        move = input("Enter move (e.g. e2 e4): ")
        start, end = parse_move(move)
        if not start or not end:
            continue

        piece = board.get_piece(start)
        if piece is None:
            print("No piece there.")
            continue

        if piece.color != turn:
            print("That’s not your piece.")
            continue

        moved = board.move_piece(start, end)
        if moved:
            turn = "black" if turn == "white" else "white"
        else:
            print("Invalid move.")

if __name__ == "__main__":
    main()
