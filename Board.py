from Pieces import King, Queen, Rook, Bishop, Pawn, Knight
import random
class Board:
    def __init__(self):
        self.board = self.create_board()
        self.turn = "w"
#--------------------CREATES BOARD---------------
    def create_board(self):
        board = []

        for i in range(8):
          b = []
          for j in range(8):
              b.append(None)  # add 8 blank squares to row
          board.append(b) # add this row to the board
#--------------SETUP BOARD (ADD PLAYERS)------------
        #add black player in board
        board[0][0] = Rook("black")
        board[0][1] = Knight("black")
        board[0][2] =Bishop("black")
        board[0][3] = Queen("black")
        board[0][4] = King("black")
        board[0][5] = Bishop("black")
        board[0][6] = Knight("black")
        board[0][7] = Rook("black")

        for i in range(8):
          board[1][i] = Pawn("black")

        #add white player in board
        board[7][0] = Rook("white")
        board[7][1] = Knight("white")
        board[7][2] = Bishop("white")
        board[7][3] = Queen("white")
        board[7][4] = King("white")
        board[7][5] = Bishop("white")
        board[7][6] = Knight("white")
        board[7][7] = Rook("white")

        for i in range(8):
          board[6][i] = Pawn("white")

        return board
#-------------- IDENTIFY PIECE POSITION--------
    def get_piece(self, position):
        row, col = position
        return self.board[row][col]
#---------MOVE PIECE------------
    def move_piece(self, start, end):
        piece = self.get_piece(start)

        # Check 1: Is there a piece at the start square?
        if piece is None:
            print("No piece at the selected position.")
            return False

        # Check 2: Is the piece the correct color for this turn?
        if piece.color != ("white" if self.turn == "w" else "black"):
            print("You must move your own piece.")
            return False
        # Check 3: Is it a valid move for that piece?
        if piece and piece.is_valid_move(start, end, self):
            self.board[start[0]][start[1]] = None
            self.board[end[0]][end[1]] = piece

            self.turn = "b" if self.turn == "w" else "w"
            return True

        print("That move is not valid.")
        return False


    def is_path_clear(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        row_step = (end_row - start_row)
        if row_step != 0:
            row_step //= abs(row_step)

        col_step = (end_col - start_col)
        if col_step != 0:
            col_step //= abs(col_step)

        current_row = start_row + row_step
        current_col = start_col + col_step

        while (current_row, current_col) != end:
            if self.board[current_row][current_col] is not None:
                return False  # Blocked!
            current_row += row_step
            current_col += col_step

        return True

    def show_board(self):
        print("   a  b  c  d  e  f  g  h")
        print("  ------------------------")
        for i in range(8):
    #         row_str = " ["
    #         for j in range(8):
    #             piece = self.board[i][j]
    #             row_str += (piece.symbol if piece else ".") + " "
    #             # row_str = row_str + self.board[i][j] + " "
    #         row_str = row_str + "] "
    #         print(row_str)
    #     print("  ------------------------")
    #     print("   a  b  c  d  e  f  g  h\n")
    #
    # def show_board(self):
    #     print("   a  b  c  d  e  f  g  h")
    #     print("  ------------------------")
    #     for i in range(8):
            row_str = f"{8 - i} | "
            for j in range(8):
                piece = self.board[i][j]
                row_str += (piece.symbol if hasattr(piece, "symbol") else ".") + " "
            row_str += f"| {8 - i}"
            print(row_str)
        print("  ------------------------")
        print("   a  b  c  d  e  f  g  h\n")


    def get_all_valid_moves(self, color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    for r in range(8):
                        for c in range(8):
                            start = (row, col)
                            end = (r, c)
                            try:
                                if piece.is_valid_move(start, end, self):
                                    if isinstance(piece, (Rook, Bishop, Queen)) and not self.is_path_clear(start, end):
                                        continue
                                    valid_moves.append((start, end))
                            except NotImplementedError:
                                print(f"Piece at {start} is missing is_valid_move: {piece.__class__.__name__}")
        return valid_moves

