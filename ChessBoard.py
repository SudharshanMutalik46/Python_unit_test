from ChessBoard import ChessBoard
from ChessRules import ChessRules

# Creating objects of Chessboard and ChessRules class
cb = ChessBoard(0)  # Create a chess board object with the initial position
chess_rules_obj = ChessRules()

# Assuming the is_checkmate method is correctly implemented in the ChessRules class
# and it checks if the black player is in checkmate
is_checkmate_result = chess_rules_obj.is_checkmate(cb.GetState(), "black")

# Use the result as needed, for example:
if is_checkmate_result:
    print("Black player is in checkmate.")
else:
    print("Black player is not in checkmate.")
