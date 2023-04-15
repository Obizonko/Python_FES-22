from board import Board

class Game:
    def __init__(self):
        self.black_king = None
        self.white_king = None
        self.color = 'white'
        self.b = Board()

    def initialize(self):
        self.b.generate_figures()
        self.white_king = self.b.get_figure_by_location(3, 0)
        self.black_king = self.b.get_figure_by_location(3, 7)

    def run(self):
        while True:
            self.b.show_grid()
            if self.white_king.get_live_status() is False or self.black_king.get_live_status() is False:
                print("\nThe end")
                break
            print('\nChoose the elem ')
            location = input()
            x, y = location.split()
            elem = self.b.get_figure_by_location(int(x), int(y))
            if elem is None:
                continue
            if elem.location != (x, y):
                elem.set_location((int(x), int(y)))
            print('Choose location to place the elem')
            location = input()
            x, y = location.split()
            self.b.place_piece(int(x), int(y), elem)
            self.b.reverse_grid()


g = Game()
g.initialize()
g.run()