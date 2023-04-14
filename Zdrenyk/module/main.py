class GameFactory:
    def create_board(self):
        pass

    def create_piece(self, piece_type, color):
        pass

    def create_game(self):
        pass


class ChessFactory(GameFactory):
    def create_board(self):
        return ChessBoard()

    def create_piece(self, piece_type, color):
        return ChessPiece(piece_type, color)

    def create_game(self):
        return ChessGame()


class Board:
    def __init__(self, size):
        self._size = size


class ChessBoard(Board):
    def __init__(self):
        super().__init__(8)


class Piece:
    def __init__(self, piece_type, color):
        self._piece_type = piece_type
        self._color = color


class ChessPiece(Piece):
    def __init__(self, piece_type, color):
        super().__init__(piece_type, color)


class Game:
    def __init__(self, board, players):
        self._board = board
        self._players = players


class ChessGame(Game):
    def __init__(self):
        board = ChessFactory().create_board()
        pieces = [ChessFactory().create_piece("pawn", "white"),
                  ChessFactory().create_piece("rook", "white"),
                  ChessFactory().create_piece("bishop", "white"),
                  ChessFactory().create_piece("knight", "white"),
                  ChessFactory().create_piece("queen", "white"),
                  ChessFactory().create_piece("king", "white"),
                  ChessFactory().create_piece("pawn", "black"),
                  ChessFactory().create_piece("rook", "black"),
                  ChessFactory().create_piece("bishop", "black"),
                  ChessFactory().create_piece("knight", "black"),
                  ChessFactory().create_piece("queen", "black"),
                  ChessFactory().create_piece("king", "black")]
        players = ["white", "black"]
        super().__init__(board, players)

        class Piece:
            def __init__(self, position, color):
                self.position = position
                self.color = color
                self.possible_moves = []

            def move(self, position):
                self.position = position

            def get_color(self):
                return self.color

            def get_position(self):
                return self.position

            def get_possible_moves(self):
                return self.possible_moves

            class Pawn(Piece):
                def __init__(self, color):
                    super().__init__(color)
                    self.name = "Pawn"
                    self.symbol = "P"

                def get_possible_moves(self, x, y, board):
                    possible_moves = []
                    if self.color == "white":
                        if x > 0 and board[x - 1][y] is None:
                            possible_moves.append((x - 1, y))
                            if x == 6 and board[x - 2][y] is None:
                                possible_moves.append((x - 2, y))
                        if x > 0 and y > 0 and board[x - 1][y - 1] is not None and board[x - 1][
                            y - 1].color != self.color:
                            possible_moves.append((x - 1, y - 1))
                        if x > 0 and y < 7 and board[x - 1][y + 1] is not None and board[x - 1][
                            y + 1].color != self.color:
                            possible_moves.append((x - 1, y + 1))
                    else:
                        if x < 7 and board[x + 1][y] is None:
                            possible_moves.append((x + 1, y))
                            if x == 1 and board[x + 2][y] is None:
                                possible_moves.append((x + 2, y))
                        if x < 7 and y > 0 and board[x + 1][y - 1] is not None and board[x + 1][
                            y - 1].color != self.color:
                            possible_moves.append((x + 1, y - 1))
                        if x < 7 and y < 7 and board[x + 1][y + 1] is not None and board[x + 1][
                            y + 1].color != self.color:
                            possible_moves.append((x + 1, y + 1))
                    return possible_moves

            class Knight(Piece):
                def __init__(self, color):
                    super().__init__(color)
                    self.name = "Knight"
                    self.symbol = "N"

                def get_possible_moves(self, x, y, board):
                    possible_moves = []
                    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
                    for dx, dy in moves:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                            if board[new_x][new_y] is None or board[new_x][new_y].color != self.color:
                                possible_moves.append((new_x, new_y))
                    return possible_moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'B'
        self.value = 3

    def get_moves(self, board, row, col):
        moves = []
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col - i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col - i):
                break
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'R'
        self.value = 5

    def get_moves(self, board, row, col):
        moves = []
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row, col - i):
                break
        return moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Q'
        self.value = 9

    def get_moves(self, board, row, col):
        moves = []
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row, col - i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row + i, col - i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col + i):
                break
        for i in range(1, 8):
            if self._add_if_valid(moves, board, row - i, col - i):
                break
        return moves

    class King(Piece):
        def __init__(self, color):
            super().__init__("King", color)

        def can_move(self, start, end, board):
            x1, y1 = start
            x2, y2 = end

            if board[x2][y2] is not None and board[x2][y2].color == self.color:
                return False

            if abs(x1 - x2) > 1 or abs(y1 - y2) > 1:
                return False

            return True

        class Board:
            def __init__(self):
                self.board = [[' ' for i in range(8)] for j in range(8)]
            def print_board(self):
                for i in range(8):
                    print('+---+---+---+---+---+---+---+---+')
                    for j in range(8):
                        print(f'| {self.board[i][j]} ', end='')
                    print('|')
                print('+---+---+---+---+---+---+---+---+')

            def is_valid_move(self, piece, start, end):

                if not (0 <= start[0] <= 7 and 0 <= start[1] <= 7 and 0 <= end[0] <= 7 and 0 <= end[1] <= 7):
                    return False

                if self.board[start[0]][start[1]] != piece.symbol:
                    return False

                if self.board[end[0]][end[1]] != ' ' and self.board[end[0]][end[1]].isupper() == piece.color.isupper():
                    return False

                if not piece.can_move(start, end, self.board):
                    return False

                return True

            def move_piece(self, piece, start, end):

                if not self.is_valid_move(piece, start, end):
                    return False

                self.board[end[0]][end[1]] = piece.symbol
                self.board[start[0]][start[1]] = ' '

                return True

            class Game:
                def __init__(self):
                    self.board = Board()  # create a new chess board
                    self.players = ['white', 'black']  # define the players
                    self.current_player = self.players[0]  # set the current player to white
                    self.move_count = 1  # keep track of the move count

                def switch_player(self):
                    """Switch the current player"""
                    if self.current_player == self.players[0]:
                        self.current_player = self.players[1]
                    else:
                        self.current_player = self.players[0]

                def get_input(self):
                    """Get user input for the next move"""
                    print(f"{self.current_player}'s move")
                    from_pos = input("Enter starting position (e.g. 'e2'): ")
                    to_pos = input("Enter destination position (e.g. 'e4'): ")
                    return from_pos, to_pos

                def play(self):
                    """Start the game loop"""
                    while True:
                        # print the board and get user input
                        print(self.board)
                        from_pos, to_pos = self.get_input()

                        # check if the move is valid
                        if not self.board.is_valid_move(from_pos, to_pos, self.current_player):
                            print("Invalid move! Try again.")
                            continue

                        # make the move and check for checkmate
                        self.board.make_move(from_pos, to_pos)
                        if self.board.is_checkmate(self.current_player):
                            print(f"Checkmate! {self.current_player} wins!")
                            break

                        # switch players and increment the move count
                        self.switch_player()
                        self.move_count += 1
                        from abc import ABC, abstractmethod

                        # Abstract classes
                        class AbstractBoard(ABC):
                            @abstractmethod
                            def is_valid_move(self, piece, move):
                                pass

                            @abstractmethod
                            def make_move(self, piece, move):
                                pass

                        class PieceFactory:
                            @staticmethod
                            def create_piece(piece_type):
                                if piece_type == PieceType.PAWN:
                                    return Pawn()
                                elif piece_type == PieceType.KNIGHT:
                                    return Knight()
                                elif piece_type == PieceType.BISHOP:
                                    return Bishop()
                                elif piece_type == PieceType.ROOK:
                                    return Rook()
                                elif piece_type == PieceType.QUEEN:
                                    return Queen()
                                elif piece_type == PieceType.KING:
                                    return King()
                                else:
                                    return None

                        class GameFactory:
                            _instance = None

                            @staticmethod
                            def get_instance():
                                if GameFactory._instance is None:
                                    GameFactory._instance = Game()
                                return GameFactory._instance

                        # Concrete classes
                        class Board(AbstractBoard):
                            def __init__(self):
                                # initialize board here
                                pass

                            def is_valid_move(self, piece, move):
                                # implement move validation logic here
                                pass

                            def make_move(self, piece, move):
                                # implement move execution logic here
                                pass

                            class Piece:
                                def __init__(self, color):
                                    self.color = color

                            class Pawn(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class Knight(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class Bishop(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class Rook(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class Queen(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class King(Piece):
                                def __init__(self, color):
                                    super().__init__(color)

                            class Board:
                                def __init__(self):
                                    self.board = [[None for _ in range(8)] for _ in range(8)]

                                def is_valid_move(self, start, end):
                                    # TODO: implement valid move check
                                    pass

                                def move(self, start, end):
                                    # TODO: implement move
                                    pass

                            class Game:
                                def __init__(self):
                                    self.board = Board()
                                    self.white_pieces = [Pawn('white'), Knight('white'), Bishop('white'), Rook('white'),
                                                         Queen('white'), King('white')]
                                    self.black_pieces = [Pawn('black'), Knight('black'), Bishop('black'), Rook('black'),
                                                         Queen('black'), King('black')]

                                def is_valid_move(self, start, end):
                                    return self.board.is_valid_move(start, end)

                                def move(self, start, end):
                                    if self.is_valid_move(start, end):
                                        self.board.move(start, end)
                                    else:
                                        print("Invalid move!")

                                def check(self, color):
                                    # TODO: implement check checking
                                    pass

                                def checkmate(self, color):
                                    # TODO: implement checkmate checking
                                    pass
