import pieces, random

piece_classes = {
    "Rook": pieces.Rook,
    "Knight": pieces.Knight,
    "Bishop": pieces.Bishop,
    "Queen": pieces.Queen,
    "King": pieces.King,
    "Pawn": pieces.Pawn
}
piece_types = ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]


class Game:
    def __init__(self):
        self.board = Board()
        self.board.fill_normal()
        self.turn = "blue"
        self.checkmate = False

    def play(self) -> None:
        """
        Play the game
        :return: None
        """
        while True:
            print(self.board.generate_string(True))
            move = input("Enter your move (e.g. a1a2): ")
            x1 = self.board.letters.index(move[0])
            y1 = 8 - int(move[1])
            x2 = self.board.letters.index(move[2])
            y2 = 8 - int(move[3])
            if self.board.move(x1, y1, x2, y2):
                print("Valid move")
            else:
                print("Invalid move")


class Board:
    def __init__(self):
        self.size = 8
        self.map = [[None for i in range(self.size)] for j in range(self.size)]
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.kings = {"blue": None, "red": None}
        self.turn = "blue"
        # color escape codes
        self.cec = {
            "blue": "\033[94m", # Red
            "red": "\033[91m", # Blue
            "r": "\033[0m", # reset
            "green": "\033[92m", # Green
            "yellow": "\033[93m", # Yellow
        }

    def __str__(self):
        return str(self.board)

    def fill_normal(self) -> None:
        """
        Fill the board with random pieces (not finished)
        :return: None
        """
        # Define the pieces and their starting positions for each color
        pieces_names = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        create_piece = {
            "Rook": pieces.Rook,
            "Knight": pieces.Knight,
            "Bishop": pieces.Bishop,
            "Queen": pieces.Queen,
            "King": pieces.King,
            "Pawn": pieces.Pawn
        }
        starting_row = [0, 7]
        colors = ["red", "blue"]

        # Place the blue pieces
        for i, piece in enumerate(pieces_names):
            self.map[starting_row[0]][7 - i] = create_piece[piece](colors[0], 7 - i, starting_row[0])
        for i in range(8):
            self.map[starting_row[0] + 1][i] = create_piece["Pawn"](colors[0], i, starting_row[0] + 1)

        # Place the red pieces
        for i, piece in enumerate(pieces_names):
            self.map[starting_row[1]][i] = create_piece[piece](colors[1], i, starting_row[1])
        for i in range(8):
            self.map[starting_row[1] - 1][i] = create_piece["Pawn"](colors[1], i, starting_row[1] - 1)

        self.kings["blue"] = self.map[starting_row[0]][4]
        self.kings["red"] = self.map[starting_row[1]][4]

    def fill_random(self, steps: int = 100, show: bool = False) -> None:
        self.fill_normal()

    #     perform few random moves
        for i in range(steps):
            available_moves = []
            for y in range(self.size):
                for x in range(self.size):
                    if self.map[y][x] is not None and self.map[y][x].color == self.turn:
                        available_moves += self.map[y][x].generate_moves(self)
            if len(available_moves) > 0:
                move = random.choice(available_moves)
                status = self.move(move[0], move[1], move[2], move[3])
                while not status:
                    available_moves.remove(move)
                    if len(available_moves) > 0:
                        move = random.choice(available_moves)
                        status = self.move(move[0], move[1], move[2], move[3])
                    else:
                        break
                if show:
                    move_str = f"{8 - move[1]}{self.letters[move[0]]}{8 - move[3]}{self.letters[move[2]]}"
                    print(f"Move {i + 1}: {self.cec['green']}{move_str}{self.cec['r']}")
                    print(self.generate_string(True), end="\n\n")
            else:
                break

        if show:
            print("Generated board:")

    def general_move_check(self, x1: int, y1: int, x2: int, y2: int, turn_color: str) -> bool:
        """
        Check if the move is valid
        :param x1: starting x position
        :param y1: starting y position
        :param x2: target x position
        :param y2: target y position
        :return: True if the move is valid, False otherwise
        """

        # Check if the move is within the board
        if 0 <= x1 < self.size and 0 <= y1 < self.size and 0 <= x2 < self.size and 0 <= y2 < self.size:
            # Check if the target is not the same position
            if not (x1 == x2 and y1 == y2):
                # Check if the target position is empty or has a piece of the opposite color
                if self.map[y1][x1].color == turn_color and \
                        (self.map[y2][x2] is None or self.map[y2][x2].color != self.map[y1][x1].color):
                    return True
        else:
            return False

    def move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Move a piece from (x1, y1) to (x2, y2)
        :param x1: starting x position
        :param y1: starting y position
        :param x2: target x position
        :param y2: target y position
        :return: True if the move is valid, False otherwise
        """
        # checkmate_before = self.check_for_checkmate()

        if self.general_move_check(x1, y1, x2, y2, self.turn):
            if self.map[y1][x1].check_move(self.map, x2, y2):
                if self.map[y1][x1].name == "Pawn":
                    self.map[y1][x1].has_moved = True

                temp = self.map[y2][x2]
                self.map[y2][x2] = self.map[y1][x1]
                self.map[y2][x2].x = x2
                self.map[y2][x2].y = y2
                self.map[y1][x1] = None

                checkmate_after = self.check_for_checkmate()
                if checkmate_after:
                    self.map[y1][x1] = self.map[y2][x2]
                    self.map[y1][x1].x = x1
                    self.map[y1][x1].y = y1
                    self.map[y2][x2] = temp
                    return False

                self.turn = "red" if self.turn == "blue" else "blue"
                return True
        return False

    def check_for_checkmate(self) -> bool:
        """
        Check if the king is in checkmate
        :return: True if the king is in checkmate, False otherwise
        """
        for y in range(self.size):
            for x in range(self.size):
                if self.map[y][x] is not None and self.map[y][x].color != self.turn:
                    for move in self.map[y][x].generate_moves(self):
                        if self.map[move[3]][move[2]] is not None and self.map[move[3]][move[2]].name == "King":
                            return True
        return False

    def generate_string(self, special_info: bool = False) -> str:
        """
        Generate a string representation of the board
        :return: The string representation of the board
        """
        string_rows = []
        string_rows.append("    A B C D E F G H ")
        string_rows.append("  +----------------+")
        for i in range(8):
            row = []
            for j in range(8):
                if self.map[i][j] is None:
                    row.append(" ")
                else:
                    row.append(
                        self.cec[self.map[i][j].color] +
                        self.map[i][j].symbol +
                        self.cec["r"])
            string_rows.append(str(8 - i) + " | " + " ".join(row) + " | " + str(8 - i))
        string_rows.append("  +----------------+")
        string_rows.append("    A B C D E F G H ")

        if special_info:
            string_rows[0] += f"    Turn: {self.cec[self.turn]}{self.turn}{self.cec['r']}"
            pieces_left = {"blue": 0, "red": 0}
            for i in range(8):
                for j in range(8):
                    if self.map[i][j] is not None:
                        pieces_left[self.map[i][j].color] += 1
            string_rows[1] += f"    Left pieces: " \
                              f"{pieces_left['blue']} {self.cec['blue']}blue{self.cec['r']}, " \
                              f"{pieces_left['red']} {self.cec['red']}red{self.cec['r']}"

            for i, piece_type in enumerate(piece_types):
                piece = piece_classes[piece_type](self.turn, 0, 0)
                string_rows[3 + i] += f"    {piece.symbol} = {piece.name}, {piece.value} points"

        return "\n".join(string_rows)
