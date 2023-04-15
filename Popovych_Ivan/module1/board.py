from figures import Pawn, Rook, Knight, Bishop, King, Queen, Piece
from utils import check_correct_move
import numpy as np


class Board:
    def __init__(self):
        self.grid = np.array([[None for _ in range(8)] for _ in range(8)])

    def generate_figures(self):
        for i in range(8):
            self.grid[i][1] = Pawn("white", (i, 1))
        self.grid[0][0] = Rook("white", (0, 0))
        self.grid[1][0] = Knight("white", (1, 0))
        self.grid[2][0] = Bishop("white", (2, 0))
        self.grid[3][0] = King("white", (3, 0))
        self.grid[4][0] = Queen("white", (4, 0))
        self.grid[5][0] = Bishop("white", (5, 0))
        self.grid[6][0] = Knight("white", (6, 0))
        self.grid[7][0] = Rook("white", (7, 0))

        for i in range(8):
            self.grid[i][6] = Pawn("black", (i, 6))
        self.grid[0][7] = Rook("black", (0, 7))
        self.grid[1][7] = Knight("black", (1, 7))
        self.grid[2][7] = Bishop("black", (2, 7))
        self.grid[3][7] = King("black", (3, 7))
        self.grid[4][7] = Queen("black", (4, 7))
        self.grid[5][7] = Bishop("black", (5, 7))
        self.grid[6][7] = Knight("black", (6, 7))
        self.grid[7][7] = Rook("black", (7, 7))

    def place_piece(self, x, y, piece: Piece):
        if not isinstance(piece, Piece):
            raise TypeError("Expected a Piece object")
        if check_correct_move(x, y) is False:
            print('incorrect data')
            return
        bool = False
        piece.generate_moves()
        loc_arr = piece.get_possible_moves()
        if (x, y) in loc_arr:
            bool = True
            loc_arr2 = piece.get_possible_moves_history()
            loc_arr2 = loc_arr2[(x, y)]
            if loc_arr2:
                for (x2, y2) in loc_arr2:
                    if self.grid[x2][y2] and self.grid[x2][y2] != piece:
                        print("There is already an element on the route")
                        bool = False
                        break
        else:
            print("A figure can't walk like that")

        if bool:
            elem = self.grid[x][y]
            if elem and elem.color != piece.color:
                elem.set_unlive()
            loc = piece.get_location()
            x1 = loc[0]
            y1 = loc[1]
            self.grid[x1][y1] = None
            self.grid[x][y] = piece
            piece.set_location((x, y))

    def get_figure_by_location(self, x, y):
        return self.grid[x][y]

    def show_figure(self, value):
        if isinstance(value, Piece):
            return value.name
        else:
            return '.'

    def reverse_grid(self):
        temp = np.array(self.grid)
        self.grid = np.fliplr(temp)

    def show_grid(self):
        for x in range(8):
            print('')
            for y in range(8):
                print(f'| {self.show_figure(self.grid[x][y])} |', end=' ')