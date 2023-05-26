class Piece:
    """
    The base class for all pieces
    """
    def __init__(self, color: str, x: int, y: int, name: str, value: float, symbol: str):
        if color not in ["blue", "red"]:
            raise ValueError("Invalid color")
        self.color = color
        self.x = x
        self.y = y
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y})"

    def check_move(self, board_map: list[list], x: int, y: int) -> bool:
        """
        Check if the move is valid
        :param board_map: the board
        :param x: target x position
        :param y: target y position
        :return: True if the move is valid, False otherwise
        """
        return False

    def generate_moves(self, board) -> list[tuple[int, int, int, int]]:
        """
        Generate all possible moves
        :param board: the board
        :return: a list of all possible moves
        """
        return []


class King(Piece):
    """
    The king can move one square in any direction,
    so long as that square is not attacked by an enemy piece.
    """
    def __init__(self, color, x: int, y: int):
        super().__init__(color, x, y, "King", 1000, "K")

    def check_move(self, board_map, x, y) -> bool:
        if abs(x - self.x) <= 1 and abs(y - self.y) <= 1:
            return True
        return False

    def generate_moves(self, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if board.general_move_check(self.x, self.y, self.x + i, self.y + j, self.color):
                    if self.check_move(board.map, self.x + i, self.y + j):
                        moves.append((self.x, self.y, self.x + i, self.y + j))
        return moves


class Queen(Piece):
    """
    The queen combines the power of a rook and bishop.
    """
    def __init__(self, color, x, y):
        super().__init__(color, x, y, "Queen", 9, "Q")

    def check_move(self, board_map, x, y):
        # check if the move diagonal, horizontal or vertical
        if abs(x - self.x) == abs(y - self.y) or x == self.x or y == self.y:
            # check if the move is blocked
            dx = 1 if x > self.x else -1 if x < self.x else 0
            dy = 1 if y > self.y else -1 if y < self.y else 0

            # check if the path is blocked
            i, j = self.x + dx, self.y + dy
            while i != x or j != y:
                if board_map[j][i] is not None:
                    return False
                i += dx
                j += dy
            return True

    def generate_moves(self, board):
        moves = []
        for i in range(-7, 8):
            if board.general_move_check(self.x, self.y, self.x + i, self.y + i, self.color):
                if self.check_move(board.map, self.x + i, self.y + i):
                    moves.append((self.x, self.y, self.x + i, self.y + i))

            if board.general_move_check(self.x, self.y, self.x + i, self.y - i, self.color):
                if self.check_move(board.map, self.x + i, self.y - i):
                    moves.append((self.x, self.y, self.x + i, self.y - i))

            if board.general_move_check(self.x, self.y, self.x + i, self.y, self.color):
                if self.check_move(board.map, self.x + i, self.y):
                    moves.append((self.x, self.y, self.x + i, self.y))

            if board.general_move_check(self.x, self.y, self.x, self.y + i, self.color):
                if self.check_move(board.map, self.x, self.y + i):
                    moves.append((self.x, self.y, self.x, self.y + i))
        return moves


class Rook(Piece):
    """
    The rook moves horizontally or vertically, through any number of unoccupied squares.
    """
    def __init__(self, color, x, y):
        super().__init__(color, x, y, "Rook", 5, "R")

    def check_move(self, board_map, x, y):
        # check if the move is horizontal or vertical
        if x == self.x or y == self.y:
            # check if the move is blocked
            dx = 1 if x > self.x else -1 if x < self.x else 0
            dy = 1 if y > self.y else -1 if y < self.y else 0

            # check if the path is blocked
            i, j = self.x + dx, self.y + dy
            while i != x or j != y:
                if board_map[j][i] is not None:
                    return False
                i += dx
                j += dy
            return True

    def generate_moves(self, board):
        moves = []
        for i in range(-7, 8):
            if board.general_move_check(self.x, self.y, self.x + i, self.y, self.color):
                if self.check_move(board.map, self.x + i, self.y):
                    moves.append((self.x, self.y, self.x + i, self.y))

            if board.general_move_check(self.x, self.y, self.x, self.y + i, self.color):
                if self.check_move(board.map, self.x, self.y + i):
                    moves.append((self.x, self.y, self.x, self.y + i))
        return moves


class Bishop(Piece):
    """
    The bishop moves diagonally, through any number of unoccupied squares.
    """
    def __init__(self, color, x, y):
        super().__init__(color, x, y, "Bishop", 3, "B")

    def check_move(self, board_map, x, y):
        # check if the move is diagonal
        if abs(x - self.x) == abs(y - self.y):
            # check if the move is blocked
            dx = 1 if x > self.x else -1 if x < self.x else 0
            dy = 1 if y > self.y else -1 if y < self.y else 0

            # check if the path is blocked
            i, j = self.x + dx, self.y + dy
            while i != x or j != y:
                if board_map[j][i] is not None:
                    return False
                i += dx
                j += dy
            return True

    def generate_moves(self, board):
        moves = []
        for i in range(-7, 8):
            if board.general_move_check(self.x, self.y, self.x + i, self.y + i, self.color):
                if self.check_move(board.map, self.x + i, self.y + i):
                    moves.append((self.x, self.y, self.x + i, self.y + i))

            if board.general_move_check(self.x, self.y, self.x + i, self.y - i, self.color):
                if self.check_move(board.map, self.x + i, self.y - i):
                    moves.append((self.x, self.y, self.x + i, self.y - i))
        return moves


class Knight(Piece):
    """
    The knight is the only piece that can "jump" over other pieces.
    It moves in an L-shape pattern, making it a unique piece.
    """
    def __init__(self, color, x, y):
        super().__init__(color, x, y, "Knight", 3, "N")

    def check_move(self, board_map, x, y):
        if abs(x - self.x) == 2 and abs(y - self.y) == 1:
            return True
        elif abs(x - self.x) == 1 and abs(y - self.y) == 2:
            return True
        return False

    def generate_moves(self, board):
        moves = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if board.general_move_check(self.x, self.y, self.x + i, self.y + j, self.color):
                    if self.check_move(board.map, self.x + i, self.y + j):
                        moves.append((self.x, self.y, self.x + i, self.y + j))
        return moves


class Pawn(Piece):
    """
    The pawn moves forward one or two squares on its first move
    and can capture diagonally.
    """

    def __init__(self, color, x, y):
        super().__init__(color, x, y, "Pawn", 1, "P")
        self.has_moved = False

    def check_move(self, board_map, x, y):
        if self.has_moved:
            if self.color == "blue":
                if y == self.y - 1 and x == self.x:
                    return True
                elif y == self.y - 1 and abs(x - self.x) == 1 and board_map[y][x] is not None:
                    return True
                else:
                    return False
            else:
                if y == self.y + 1 and x == self.x:
                    return True
                elif y == self.y + 1 and abs(x - self.x) == 1 and board_map[y][x] is not None:
                    return True
                else:
                    return False
        else:
            if self.color == "blue":
                if y == self.y - 1 and x == self.x:
                    return True
                elif y == self.y - 2 and x == self.x:
                    return True
                elif y == self.y - 1 and abs(x - self.x) == 1 and board_map[y][x] is not None:
                    return True
                else:
                    return False
            else:
                if y == self.y + 1 and x == self.x:
                    return True
                elif y == self.y + 2 and x == self.x:
                    return True
                elif y == self.y + 1 and abs(x - self.x) == 1 and board_map[y][x] is not None:
                    return True
                else:
                    return False

    def generate_moves(self, board):
        moves = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if board.general_move_check(self.x, self.y, self.x + i, self.y + j, self.color):
                    if self.check_move(board.map, self.x + i, self.y + j):
                        moves.append((self.x, self.y, self.x + i, self.y + j))
        return moves
