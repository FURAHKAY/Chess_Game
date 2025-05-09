#This file will handle all the pieces involved in the game
#Logic: Every chess piece is either white or black.
#We define a base Piece class to avoid repeating code in every piece (King, Queen...)

class Piece: #a class is like a recipe for making an object.
    def __init__(self, color): #constructor to construct the object
        self.color = color
        self.symbol = "?"  # symbol is used for printing on the board (e.g., "K" for King).

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Subclasses must implement this method.")

    def say_color(self):
        print("I am", self.color)


class King(Piece):  # King inherits from Piece
        def __init__(self, color):
            super().__init__(color)  # Call parent (Piece) constructor - Inheritance => make new classes based on others
            self.symbol = "♚" if color == "white" else "♔"

        def is_valid_move(self, start, end, board): #king valid moves: one up, down left, right, diagonal
            dx = abs(end[0] - start[0])
            dy = abs(end[1] - start[1])
            return (dx == 1 and dy == 1) or (dx == 1 and dy == 0) or (dx == 0 and dy == 1) #diagonally or straight but only 1 block


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♛" if color == "white" else "♕"
    def is_valid_move(self, start, end, board): #Queen (most powerful) : diagonally, verically and horizontally with any number of squares
            dx = abs(end[0] - start[0])
            dy = abs(end[1] - start[1])
            return dx == dy or  dx == 0 and dy == 0 #diagonal or straight


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♝" if color == "white" else "♗"

    def is_valid_move(self, start, end, board):
        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])
        return dx == dy  # diagonal move


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♞" if color == "white" else "♘"

    def is_valid_move(self, start, end, board):
        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♜" if color == "white" else "♖"

    def is_valid_move(self, start, end, board):
        return start[0] == end[0] or start[1] == end[1]  # same row or column


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♟" if color == "white" else "♙"
    def is_valid_move(self, start, end, board):
        # White pawns move UP the board so their row numbers go DOWN and use -1
        # Black pawns move DOWN the board so their row numbers go UP and use +1
        direction = -1 if self.color == "white" else 1

        dx = end[0] - start[0]  # row movement (up (-1) or down (+1))
        dy = abs(end[1] - start[1])  # absolute column movement (sideways)

        # Check if there's a piece sitting at the end position (i.e opponent)
        destination_piece = board.get_piece(end)

        # Standard forward move (one square, no piece in the way)
        #s it going straight forward? (no sideways: dy == 0)
        # Is it moving in the right direction? (dx == +1 for black, -1 for white)
        # Is the end square empty? (destination_piece is None)
        if dy == 0 and dx == direction:
            return destination_piece is None

        # First move (can move two squares forward)
        #First check : Still moving straight → dy == 0 AND Moving 2 rows forward → dx == 2 or -2 depending on color
        if dy == 0 and dx == 2 * direction:
            # This pawn is only allowed to do that if it hasn't moved yet.
            # White starts on row 6 AND White starts on row 6
            start_row = 6 if self.color == "white" else 1
            # This line calculates the square in between the start and end when a pawn tries to move 2 steps — so we can check if something is blocking it.
            intermediate = (start[0] + direction, start[1])
            #Valid only if: Pawn is on the starting row, The square in front is empty, The square 2 ahead is also empty
            # Because pawns can’t jump over other pieces
            return (
                start[0] == start_row and
                board.get_piece(intermediate) is None and
                destination_piece is None
            )

        # Diagonal capture (1 step diagonal, and enemy piece there)
        #Moved 1 step diagonally AND In the right direction (up or down depending on color)
        if dy == 1 and dx == direction:
            # Valid only if there’s an enemy piece on the end square (so it can be captured)
            return (
                destination_piece is not None and
                destination_piece.color != self.color
            )

        return False


king = King("white")
print(king.color)   # Output: white
print(king.symbol)  # Output: K
