class Piece:
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color



    def __str__(self):
        return self.name

    def valid(self, startpos, endpos, Color, gameboard):
        if endpos in self.all_moves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False

    def all_moves(self, x, y, gameboard):
        print("ERROR: no movement for base class")

    def extract_move(self, x, y, gameboard, Color, intervals):
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.bounds(xtemp, ytemp):
                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def bounds(self, x, y):

        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def is_no_conflict(self, gameboard, initialColor, x, y):

        if self.bounds(x, y) and (
                ((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor): return True
        return False


chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def knights(x, y, int1, int2):
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


def kings(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
            (x - 1, y - 1)]

class Pawn(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.Color = color
        self.direction = direction  # 1 for w, -1 for b

    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        answers = []
        if (x + 1, y + self.direction) in gameboard and self.is_no_conflict(gameboard, Color, x + 1,
                                                                            y + self.direction): answers.append(
            (x + 1, y + self.direction))
        if (x - 1, y + self.direction) in gameboard and self.is_no_conflict(gameboard, Color, x - 1,
                                                                            y + self.direction): answers.append(
            (x - 1, y + self.direction))
        if (x, y + self.direction) not in gameboard and Color == self.Color: answers.append((x,
                                                                                             y + self.direction))  # the condition after the and is to make sure the non-capturing movement (the only fucking one in the game) is not used in the calculation of checkmate
        return answers

class Rook(Piece):
    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.extract_move(x, y, gameboard, Color, chessCardinals)

class Knight(Piece):
    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in knights(x, y, 2, 1) if self.is_no_conflict(gameboard, Color, xx, yy)]

class Bishop(Piece):
    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.extract_move(x, y, gameboard, Color, chessDiagonals)

class Queen(Piece):
    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.extract_move(x, y, gameboard, Color, chessCardinals + chessDiagonals)

class King(Piece):
    def all_moves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in kings(x, y) if self.is_no_conflict(gameboard, Color, xx, yy)]





WHITE = "white"
BLACK = "black"

uniDict = {
    BLACK : {
        Pawn : "♙",
        Rook : "♖",
        Knight : "♘",
        Bishop : "♗",
        King : "♔",
        Queen : "♕"
    },
    WHITE : {
        Pawn : "♟",
        Rook : "♜",
        Knight : "♞",
        Bishop : "♝",
        King : "♚",
        Queen : "♛"
    }
}