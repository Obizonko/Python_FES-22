from board import Board

class Game:
    def __init__(self):
        self.color = 'white'
        self.b = Board()

    def initialize(self):
        self.b.generate_figures()

    def run(self):
        while True:
            self.b.show_grid()
            print('\nChoose the elem ')
            location = input()
            x, y = location.split()
            elem = self.b.get_figure_by_location(int(x), int(y))
            print('Choose location to place the elem')
            location = input()
            x, y = location.split()
            self.b.place_piece(int(x), int(y), elem)


g = Game()
g.initialize()
g.run()