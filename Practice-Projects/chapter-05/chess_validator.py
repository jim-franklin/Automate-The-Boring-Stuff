
# 1 - exactly one black king and exactly one white king.
# 2 - Each player have at most 16 pieces
# 3 - Each player have at most 8 pawns
# 4 - a valid space from '1a' to '8h'
# 5 - The piece names begin with either a 'w' or 'b'
# 6 - followed by 'pawn', 'knight','bishop', 'rook', 'queen', or 'king'.

# creates and returns a dictionary for all the pieces that starts with the
# specified 'beginning_letter' and how many pieces of each type has appeared.
def dec_analysis(board, beginning_letter):
    dic = {}
    for piece_name in board.values():
        if piece_name[0] == beginning_letter:
            dic.setdefault(piece_name, 0)
            dic[piece_name] += 1
    return dic


def number_of_pieces(board):
    """given a dictionary, it returns the total of the values."""
    total = 0
    for value in board.values():
        total += value
    return total


def is_valid_chessboard(chess_board):
    valid_numbers = "123456789"
    valid_letter = "abcdefgh"
    valid_colors = 'bw'
    valid_names = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    black_pieces = dec_analysis(chess_board, 'b')
    white_pieces = dec_analysis(chess_board, 'w')

    bpawn = black_pieces.get('bpawn', 0)
    wpawn = white_pieces.get('wpawn', 0)

    total_black_pieces = number_of_pieces(black_pieces)
    total_white_pieces = number_of_pieces(white_pieces)

    # 1 - each player one black king and exactly one white king.
    if black_pieces["bking"] != 1 or white_pieces["wking"] != 1:
        print("not exatly one king error")
        return False

    # 2 - Each player have at most 16 pieces
    if total_black_pieces > 16 or total_white_pieces > 16:
        print("too much pieces for each player error")
        return False

    # 3 - Each player have at most 8 pawns
    if bpawn > 8 or wpawn > 8:
        print("too much pawns error")
        return False

    # 4 - a valid space from '1a' to '8h'
    for space in chess_board:
        if space[0] not in valid_letter:
            print("invalid space letter error in: " + space)
            return False
        if space[1] not in valid_numbers:
            print("invalid space number error in: " + space)
            return False

    # 5 - The piece names begin with either a 'w' or 'b' to represent white or black
    # 6 - followed by 'pawn', 'knight','bishop', 'rook', 'queen', or 'king'.
    for piece_name in chess_board.values():
        if piece_name[0] not in valid_colors:
            print("invalid name color error in: " + piece_name)
            return False
        if piece_name[1:] not in valid_names:
            print("invalid name member error in: " + piece_name)
            return False
    
    return True


if __name__ == "__main__":
    my_board = {
            'e3': 'wking', 'c6': 'wqueen',
            'g2': 'bbishop', 'd2': 'bqueen', 'g3': 'bking',
            'a1': 'bpawn', 'c1': 'bpawn', 'd1': 'bpawn',
            'g1': 'bpawn', 'h1': 'bpawn',
            'e2': 'bpawn', 'a2': 'bpawn'
            }
    print(is_valid_chessboard(my_board))
    