class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def __str__(self):
        return self.color[0].upper() + self.piece_type.upper()

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if self.color == 'white' and end_row <= start_row:
            return False
        elif self.color == 'black' and end_row >= start_row:
            return False
        if start_col != end_col:
            if board.get_piece(end_row, end_col) is None:
                return False
        else:
            if abs(end_row - start_row) > 2:
                return False
            elif abs(end_row - start_row) == 2 and start_row != 1 and start_row != 6:
                return False

        return True


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_pos, end_pos, board):
        piece = board.get_piece(start_pos[0], start_pos[1])
        if self.color == 'white':
            if end_pos[0] == start_pos[0] - 1 and end_pos[1] == start_pos[1] and board.get_piece(*end_pos) is None:
                return True
            elif start_pos[0] == 6 and end_pos[0] == start_pos[0] - 2 and end_pos[1] == start_pos[1] and board.get_piece(start_pos[0] - 1, start_pos[1]) is None and board.get_piece(*end_pos) is None:
                return True
            elif end_pos[0] == start_pos[0] - 1 and abs(end_pos[1] - start_pos[1]) == 1 and board.get_piece(*end_pos) is not None and board.get_piece(*end_pos).color == 'black':
                return True
        elif self.color == 'black':
            if end_pos[0] == start_pos[0] + 1 and end_pos[1] == start_pos[1] and board.get_piece(*end_pos) is None:
                return True
            elif start_pos[0] == 1 and end_pos[0] == start_pos[0] + 2 and end_pos[1] == start_pos[1] and board.get_piece(start_pos[0] + 1, start_pos[1]) is None and board.get_piece(*end_pos) is None:
                return True
            elif end_pos[0] == start_pos[0] + 1 and abs(end_pos[1] - start_pos[1]) == 1 and board.get_piece(*end_pos) is not None and board.get_piece(*end_pos).color == 'white':
                return True
        return False


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_pos, end_pos, board):
        if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:
            if start_pos[0] == end_pos[0]:
                start, end = sorted([start_pos[1], end_pos[1]])
                for i in range(start + 1, end):
                    if board.get_piece(start_pos[0], i) is not None:
                        return False
            else:
                start, end = sorted([start_pos[0], end_pos[0]])
                for i in range(start + 1, end):
                    if board.get_piece(i, start_pos[1]) is not None:
                        return False
            return board.get_piece(*end_pos) is None or board.get_piece(*end_pos).color != self.color
        return False


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_pos, end_pos, board):
        if abs(end_pos[0] - start_pos[0]) == abs(end_pos[1] - start_pos[1]):
            row, col = start_pos
            delta_row, delta_col = (1, 1) if end_pos[0] > start_pos[0] else (
                -1, -1), (1, -1) if end_pos[1] > start_pos[1] else (-1, 1)
            while (row, col) != end_pos:
                row, col = row + delta_row[0], col + delta_col[1]
                if board.get_piece(row, col) is not None:
                    return False
            return board.get_piece(*end_pos) is None or board.get_piece(*end_pos).color != self.color
        return False


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'N')

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        if row_diff == 2 and col_diff == 1:
            return True
        elif row_diff == 1 and col_diff == 2:
            return True
        else:
            return False


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, 'Q')

    def is_valid_move(self, start_pos, end_pos, board):
        x_diff = abs(start_pos[0] - end_pos[0])
        y_diff = abs(start_pos[1] - end_pos[1])
        if x_diff == 0 or y_diff == 0 or x_diff == y_diff:
            return True
        return False


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start_pos, end_pos, board):
        if abs(end_pos[0] - start_pos[0]) <= 1 and abs(end_pos[1] - start_pos[1]) <= 1:
            return board.get_piece(*end_pos) is None or board.get_piece(*end_pos).color != self.color
        return False


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def __str__(self):
        return self.color[0].upper() + self.piece_type.upper()

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if self.color == 'white' and end_row <= start_row:
            return False
        elif self.color == 'black' and end_row >= start_row:
            return False
        if start_col != end_col:
            if board.get_piece(end_row, end_col) is None:
                return False
        else:
            if abs(end_row - start_row) > 2:
                return False
            elif abs(end_row - start_row) == 2 and start_row != 1 and start_row != 6:
                return False

        return True
