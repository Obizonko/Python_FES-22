from utils import check_correct_move


class Piece:
    def __init__(self, color, location):
        self.color = color
        self.is_avile = True
        self.location = location
        self.all_moves = {}

    def set_unlive(self):
        self.is_avile = False

    def get_location(self) -> tuple:
        return self.location

    def set_location(self, location: tuple):
        self.location = location

    def set_all_moves_item(self, x, y, hist_moves=None):
        if check_correct_move(x, y):
            self.all_moves[(x, y)] = hist_moves
            return True
        return False

    def get_possible_moves_history(self):
        return self.all_moves

    def get_possible_moves(self):
        return list(self.all_moves.keys())

    def generate_moves(self):
        pass

class King(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♔"

    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        temp_x = _x
        temp_y = _y + 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x - 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x + 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_y = _y
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x - 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x
        temp_y = _y - 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x + 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        temp_x = _x - 1
        self.set_all_moves_item(temp_x, temp_y, [(temp_x, temp_y)])
        return self.all_moves


class Knight(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♘"

    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        moves = []
        moves.append((_x + 1, _y))
        moves.append((_x + 2, _y))
        self.set_all_moves_item(_x + 2, _y + 1, moves)
        self.set_all_moves_item(_x + 2, _y - 1, moves)
        moves = []
        moves.append((_x - 1, _y))
        moves.append((_x - 2, _y))
        self.set_all_moves_item(_x - 2, _y + 1, moves)
        self.set_all_moves_item(_x - 2, _y - 1, moves)
        moves = []
        moves.append((_x, _y + 1))
        moves.append((_x, _y + 2))
        self.set_all_moves_item(_x - 1, _y + 2, moves)
        self.set_all_moves_item(_x + 1, _y + 2, moves)
        moves = []
        moves.append((_x, _y - 1))
        moves.append((_x, _y - 2))
        self.set_all_moves_item(_x - 1, _y - 2, moves)
        self.set_all_moves_item(_x + 1, _y - 2, moves)


class Bishop(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♗"

    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        temp_y = loc[1]
        temp_x = loc[0]
        moves = []

        # right and down
        for i in range(1, 8):
            if i == 1:
                temp_x += 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x += 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())
        #right and up
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x -= 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x -= 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())
        #left and up
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x -= 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x -= 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())

        #left and down
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x += 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x += 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())


class Pawn(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♙"

    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        self.set_all_moves_item(_x, _y + 1)
        if _y == 1:
            self.set_all_moves_item(_x, _y+2, [(_x, _y + 1)])
        self.set_all_moves_item(_x-1, _y+1)
        self.set_all_moves_item(_x+1, _y+1)




class Queen(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♕"


    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        temp_y = loc[1]
        temp_x = loc[0]
        moves = []

        # right and down
        for i in range(1, 8):
            if i == 1:
                temp_x += 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x += 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())
        #right and up
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x -= 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x -= 1
                temp_y += 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())
        #left and up
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x -= 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x -= 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())

        #left and down
        temp_x = _x
        temp_y = _y
        moves = []
        for i in range(1, 8):
            if i == 1:
                temp_x += 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y)
            else:
                moves.append((temp_x, temp_y))
                temp_x += 1
                temp_y -= 1
                self.set_all_moves_item(temp_x, temp_y, moves.copy())

        moves = []

        for x in range(_x, 8):
            if x == 1:
                self.set_all_moves_item(x, _y)
            elif x == 0:
                continue
            else:
                moves.append((x - 1, _y))
                self.set_all_moves_item(x, _y, moves.copy())
        moves = []
        for x in range(_x, -1, -1):
            if x == 7:
                continue
            elif x == 6:
                self.set_all_moves_item(x, _y)
            else:
                moves.append((x - 1, _y))
                self.set_all_moves_item(x, _y, moves.copy())
        moves = []
        for y in range(_y, 8):
            if y == 1:
                self.set_all_moves_item(_x, y)
            elif y == 0:
                continue
            else:
                moves.append((_x, y - 1))
                self.set_all_moves_item(_x, y, moves.copy())
        moves = []
        for y in range(_y - 1, -1, -1):
            if y == 7:
                continue
            elif y == 6:
                self.set_all_moves_item(_x, y)
            else:
                moves.append((_x, y - 1))
                self.set_all_moves_item(_x, y, moves.copy())

class Rook(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.name = "♖"

    def generate_moves(self):
        loc = self.get_location()
        _x = loc[0]
        _y = loc[1]
        moves = []

        for x in range(_x, 8):
            if x == 1:
                self.set_all_moves_item(x, _y)
            elif x == 0:
                continue
            else:
                moves.append((x - 1, _y))
                self.set_all_moves_item(x, _y, moves.copy())
        moves = []
        for x in range(_x, -1, -1):
            if x == 7:
                continue
            elif x == 6:
                self.set_all_moves_item(x, _y)
            else:
                moves.append((x - 1, _y))
                self.set_all_moves_item(x, _y, moves.copy())
        moves = []
        for y in range(_y, 8):
            if y == 1:
                self.set_all_moves_item(_x, y)
            elif y == 0:
                continue
            else:
                moves.append((_x, y - 1))
                self.set_all_moves_item(_x, y, moves.copy())
        moves = []
        for y in range(_y - 1, -1, -1):
            if y == 7:
                continue
            elif y == 6:
                self.set_all_moves_item(_x, y)
            else:
                moves.append((_x, y - 1))
                self.set_all_moves_item(_x, y, moves.copy())