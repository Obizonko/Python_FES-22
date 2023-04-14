
class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def move(self, row, col):
        self.row = row
        self.col = col


class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = "king"

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = "queen"

class Rook(Piece):
    def init(self, color, row, col):
        super().init(color, row, col)
        self.type = "rook"

class Bishop(Piece):
    def init(self, color, row, col):
        super().init(color, row, col)
        self.type = "bishop"

class Knight(Piece):
    def init(self, color, row, col):
        super().init(color, row, col)
        self.type = "knight"

class Pawn(Piece):
    def init(self, color, row, col):
        super().init(color, row, col)
        self.type = "pawn"

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]


    def place_piece(self, piece):
        self.grid[piece.row][piece.col] = piece

    def get_piece(self, row, col):
        return self.grid[row][col]

    def move_piece(self, piece, row, col):
        self.grid[piece.row][piece.col] = None
        piece.move(row, col)
        self.grid[row][col] = piece
        
      

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.opponent = player2

    def switch_players(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def play(self, start_row, start_col, end_row, end_col):
        piece = self.board.get_piece(start_row, start_col)
        if piece is None:
            raise ValueError("No piece at that position")
        if piece.color != self.current_player.color:
            raise ValueError("Not your turn")
        if not self.is_valid_move(piece, end_row, end_col):
            raise ValueError("Invalid move")
        self.board.move_piece(piece, end_row, end_col)
        self.switch_players()

    def is_valid_move(self, piece, row, col):
        if piece.type == "king":
            # A king can move one square in any direction.
            if abs(piece.row - row) <= 1 and abs(piece.col - col) <= 1:
                return True
        elif piece.type == "queen":
            # A queen can move any number of squares diagonally, horizontally, or vertically.
            if piece.row == row or piece.col == col or abs(piece.row - row) == abs(piece.col - col):
                if self.path_clear(piece.row, piece.col, row, col):
                    return True
        elif piece.type == "rook":
            # A rook can move any number of squares horizontally or vertically.
            if piece.row == row or piece.col == col:
                if self.path_clear(piece.row, piece.col, row, col):
                    return True
        elif piece.type == "bishop":
            # A bishop can move any number of squares diagonally.
            if abs(piece.row - row) == abs(piece.col - col):
                if self.path_clear(piece.row, piece.col, row, col):
                    return True
        elif piece.type == "knight":
            # A knight can move in an L-shape: two squares in a straight line and then one square perpendicular to that.
            if abs(piece.row - row) == 2 and abs(piece.col - col) == 1 or abs(piece.row - row) == 1 and abs(piece.col - col) == 2:
                return True
        elif piece.type == "pawn":
            # A pawn can move one or two squares forward on its first move, and one square forward on subsequent moves. 
            # It can also capture diagonally one square forward.
            if piece.color == "white":
                if row == piece.row - 1 and col == piece.col and self.board.get_piece(row, col) is None:
                    return True
                if piece.row == 6 and row == 4 and col == piece.col and self.board.get_piece(5, col) is None and self.board.get_piece(4, col) is None:
                    return True
                if row == piece.row - 1 and abs(col - piece.col) == 1 and self.board.get_piece(row, col) is not None and self.board.get_piece(row, col).color == "black":
                    return True
            elif piece.color == "black":
                if row == piece.row + 1 and col == piece.col and self.board.get_piece(row, col) is None:
                    return True
                if piece.row == 1 and row == 3 and col == piece.col and self.board.get_piece(2, col) is None and self.board.get_piece(3, col) is None:
                    return True
                if row == piece.row + 1 and abs(col - piece.col) == 1 and self.board.get_piece(row, col) is not None and self.board.get_piece(row, col).color == "white":
                    return True
        return False