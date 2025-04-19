#assign points
#minimax


#goal to trap queen
#king moves
#queen moves

# 2-player turn-based game, where:
# Both players are humans for now
# Each one moves their own pieces, one turn at a time
# Eventually you could replace one with an AI (but not yet)

# GAME LOGIC (What we're building)
# Board setup
#
# Initialize an 8x8 board
#
# Place pieces in their correct positions
#
# Turn-taking system
#
# White moves → Black moves → repeat
#
# Keep track of whose turn it is
#
# Piece validation logic
#
# Each piece (King, Rook, etc.) knows how it can move
#
# If the move is illegal, reject it
#
# Win condition (later)
#
# Check for check, checkmate, or stalemate

#########
# INITIALIZE board
# PLACE all pieces in starting positions
#
# SET current_turn = "white"
#
# WHILE game_not_over:
#     DISPLAY board
#     PROMPT user to enter move (e.g. "e2 e4")
# CONVERT move to grid coordinates:
#   (start_row, start_col), (end_row, end_col)
#
# GET piece_at_start
#     IF no piece at start:
#         SHOW "No piece there!"
#         CONTINUE to next iteration
#
#     IF piece color is not current_turn:
#         SHOW "That's not your piece!"
#         CONTINUE
#
#     IF move is not valid for that piece:
#         SHOW "Illegal move!"
#         CONTINUE
#     ELSE MOVE piece to new position on board
#        CLEAR old position
#        SWITCH current_turn to the other player
