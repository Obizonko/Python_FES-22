from figures import Pawn, Rook, Knight, Bishop, King, Queen, Piece
from utils import check_correct_move


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

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

    def place_piece(self, x, y, piece: Piece):
        if not isinstance(piece, Piece):
            raise TypeError("Expected a Piece object")
        if check_correct_move(x, y) is False:
            print('incorrect data')
        bool = False
        piece.generate_moves()
        loc_arr = piece.get_possible_moves()
        if (x, y) in loc_arr:
            bool = True
            loc_arr2 = piece.get_possible_moves_history()
            loc_arr2 = loc_arr2[(x, y)]
            if loc_arr2:
                for (x2, y2) in loc_arr2:
                    if self.grid[x2][y2]:
                        print("There is already an element on the route")
                        bool = False
                        break

        else:
            print("A figure can't walk like that")

        if bool:
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

    def show_grid(self):
        for x in range(8):
            print('')
            for y in range(8):
                print(f'| {self.show_figure(self.grid[x][y])} |', end=' ')