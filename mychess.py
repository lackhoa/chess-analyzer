import chess

def get_protected_squares(board):
    """
    Get the squares on which pieces are protected by a piece on the same side

    :param board: The board to get protected squares
    """
    ans = chess.SquareSet()
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece is not None:
            color = piece.color
            # Question: If an enemy takes this square, will it be threatened?
            clone = board.copy()
            clone.set_piece_at(sq, chess.Piece(chess.PAWN, not color))
            if clone.is_attacked_by(color, sq):
                ans.add(sq)
    return ans
