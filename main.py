import chess.svg
import chess.pgn
import mychess

pgn = open("data/cutechess-fischerrandom.pgn")
game = chess.pgn.read_game(pgn)

# Initial position
board = game.board()
squares = chess.SquareSet()
# Highlight all the legal moves:
legal_moves = board.legal_moves
for mv in legal_moves:
    squares.add(square = mv.to_square)
# Get the legal_moves of the other guy:
board.push(chess.Move.null())
oppo_mvs = board.legal_moves
oppo_sqs = chess.SquareSet()
for mv in oppo_mvs:
    oppo_sqs.add(square = mv.to_square)
# Return control to the current guy:
board.push(chess.Move.null())
#To svg:
svg = chess.svg.board(board = board, colored_squares = [(squares, 'blue'), (oppo_sqs, 'red')], protected_squares=mychess.get_protected_squares(board))
# Write the file
with open('svg/chess0.svg', 'w+') as f:
    f.write(svg)
# Initial state variable
oppo_color = 'blue'
# Iterate through all moves and play them on a board.
counter = 0
print('Processing... Please wait')
for move in game.main_line():
    counter += 1
    #Make a move
    board.push(move)
    sqs = chess.SquareSet()
    # Highlight all the legal moves:
    mvs = board.legal_moves
    for mv in mvs:
        sqs.add(square = mv.to_square)

    # Get the legal_moves of the other guy:
    board.push(chess.Move.null())
    oppo_mvs = board.legal_moves
    oppo_sqs = chess.SquareSet()
    for mv in oppo_mvs:
        oppo_sqs.add(square = mv.to_square)
    # Return control to the current guy:
    board.push(chess.Move.null())
    # Highlight all the intersections:
    intersect = sqs & oppo_sqs
    # I don't want the colors to overlap:
    sqs = sqs.difference(intersect)
    oppo_sqs = oppo_sqs.difference(intersect)

    #To svg:
    color = 'blue' if oppo_color == "red" else 'red' # White's potential moves are blue and black's are red
    svg = chess.svg.board(board = board, colored_squares = [(sqs, color), (oppo_sqs, oppo_color)], arrows=[(move.from_square, move.to_square)], squares = intersect,  protected_squares=mychess.get_protected_squares(board))
    # Write the file
    with open('svg/chess{0}.svg'.format(counter), 'w+') as f:
        f.write(svg)
    # Record the state variables:
    oppo_color = color

print('Done!')
