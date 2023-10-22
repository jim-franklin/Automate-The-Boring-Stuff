# Analyze the chess board before checking for validity.
def boardAnalysis(board, beginning_letter):
    # create a dictionary for all the pieces that starts with the specified 'beginning_letter'
    # and how many pieces of each type has appeared.
    dic = {}
    for piece_name in board.values():
        if piece_name[0] == beginning_letter:
            dic.setdefault(piece_name, 0)
            dic[piece_name] += 1
    return dic


def totalPieces(board):
    # returns sum of values of all keys from a given dictionary.
    total = 0
    for value in board.values():
        total += value
    return total


# Check for validity
def isValidChessboard(chess_board):
    # valid variables.
    valid_space_numbers = "12345678"
    valid_space_letters = "abcdefgh"
    valid_piece_colors = "bw"
    valid_piece_names = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king'] 

    # create separate dictionaries for both black and white pieces.
    black_pieces = boardAnalysis(chess_board, 'b')
    white_pieces = boardAnalysis(chess_board, 'w')

    # fish out the value of black or white pawns from each dictionary created
    # above using the .get() function.
    # .get() will return zero if item does not exist in the dictionary.
    black_pawn = black_pieces.get('bpawn', 0)
    white_pawn = white_pieces.get('wpawn', 0)
    
    # calculate the total of black and white pieaces.
    total_black_pieces = totalPieces(black_pieces)
    total_white_pieces = totalPieces(white_pieces)

    # 1 - Exactly black king and exactly one white king.
    if black_pieces["bking"] != 1 or white_pieces["wking"] != 1:
        print("Board Error: There is not exatly one black king or white king.")
        return False

    # 2 - Each player can only have at most 16 pieces.
    if total_black_pieces > 16 or total_white_pieces > 16:
        print("Board Error: There are more than 16 pieces for at least one player")
        return False

    # 3 - Each player can only have at most 8 pawns.
    if black_pawn > 8 or white_pawn > 8:
        print("Board Error: There are more than 8 pawns for at least one player")
        return False

    # 4 - All pieces must be on a valid space from '1a' to '8h'.
    for space, piece_name in chess_board.items():
        if space[0] not in valid_space_numbers:
            print("Board Error: Invalid space-number in `" + space + ": " + piece_name + "`")
            return False
        # the rest of `space` must be only one letter, preventing double letters error
        if space[1:] not in valid_space_letters:    
            print("Board Error: Invalid space-letter in `" + space + ": " + piece_name + "`")
            return False
        
    # 5 - The piece names begin with either a 'w' or 'b' to represent white or black,
    # 6 - followed by 'pawn', 'knight','bishop', 'rook', 'queen', or 'king'.
    for space, piece_name in chess_board.items():
        if piece_name[0] not in valid_piece_colors:
            print("Board Error: Invalid piece-color `" + space + ": " + piece_name + "`")
            return False
        if piece_name[1:] not in valid_piece_names:
            print("Board Error: Invalid piece-name in: `" + space + ": " + piece_name + "`")
            return False
        
    # Return True if all requirements have been satified up to this point.
    return True

# sample chess boad with piecea
my_board = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'
    }

# call the function and print its result
print(isValidChessboard(my_board))
