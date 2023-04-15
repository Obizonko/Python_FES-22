from pieces import *
import random


class Engine:
    def __init__(self):
        self.playersturn = WHITE
        self.message = ''
        self.gameboard = {}
        self.is_active = True
        self.setup_board()
        print('Приклад ходу c3 e5')
        self.run()

    def setup_board(self):
        self.gameboard[(random.randint(2, 5), 0)] = King(WHITE, uniDict[WHITE][King])
        self.gameboard[(random.randint(2, 5), 7)] = King(BLACK, uniDict[BLACK][King])

        w_figures_count, b_figures_count = random.randint(5, 10), random.randint(5, 10)

        self.place_figures(WHITE, w_figures_count)
        self.place_figures(BLACK, b_figures_count)

    def place_figures(self, color, figures_count):
        figures_av = {
            Queen: 1,
            Rook: 2,
            Knight: 2,
            Bishop: 2,
            Pawn: 8
        }

        figures = [Rook, Knight, Bishop, Queen, Pawn]

        for i in range(figures_count):
            figure_type = figures[random.randint(0, len(figures) - 1)]

            figure = Piece(None, None)  # mock to save it for bigger scope
            if figure_type == Pawn:
                figure = figure_type(color, uniDict[color][figure_type], 1 if color == WHITE else -1)
            else:
                figure = figure_type(color, uniDict[color][figure_type])
            self.placing_figures_on_board(figure)

            figures_av[figure_type] -= 1
            if figures_av[figure_type] == 0:
                figures.remove(figure_type)

    def placing_figures_on_board(self, figure):
        is_field_set = False

        while is_field_set == False:
            pretended_field = (0, 0)

            if hasattr(figure, 'direction'):
                if figure.Color == WHITE:
                    pretended_field = (random.randint(0, 8), random.randint(1, 4))
                else:
                    pretended_field = (random.randint(0, 8), random.randint(3, 6))
            else:
                pretended_field = (random.randint(0, 8), random.randint(0, 8))

            if pretended_field not in self.gameboard:  # if no one is there
                is_field_set = True
                self.gameboard[pretended_field] = figure

        if self.check() == True:  # if check regenerate so that we get
            del self.gameboard[pretended_field]
            self.placing_figures_on_board(figure)

    def check(self):
        kingDict = {}
        pieceDict = {BLACK: [], WHITE: []}
        for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            pieceDict[piece.Color].append((piece, position))

        if self.king_reachable(kingDict[WHITE], pieceDict[BLACK]):
            self.message = 'Шах білим'
            return True
        if self.king_reachable(kingDict[BLACK], pieceDict[WHITE]):
            self.message = 'Шах чорним'
            return True

        self.message = ''
        return False

    def mate(self):
        kingDict = {}
        for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position

        if WHITE not in kingDict:
            self.message = '1 - 0 чорні перемогли'
            return True
        if BLACK not in kingDict:
            self.message = '1 - 0 білі перемогли'
            return True

        return False

    def parse_prompt(self):
        try:
            a, b = input().split()
            a = ((ord(a[0]) - 97), int(a[1]) - 1)
            b = (ord(b[0]) - 97, int(b[1]) - 1)
            print(a, b)
            return (a, b)
        except:
            print('Помилка декодування входу')
            return ((-1, -1), (-1, -1))

    def king_reachable(self, kingpos, piecelist):
        for piece, position in piecelist:
            if piece.valid(position, kingpos, piece.Color, self.gameboard):
                return True

        return False

    def render(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(8):
            print("-" * 32)
            print(chr(i + 97), end="|")
            for j in range(8):
                item = self.gameboard.get((i, j), " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 32)

    def run(self):
        while self.is_active:  # while game has not ended
            self.render()
            print(self.message)
            self.message = ''
            startpos, endpos = self.parse_prompt()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = 'Неможливо знайти фігуру'
                target = None

            if target:
                print('found ' + str(target))
                if target.Color != self.playersturn:
                    self.message = "Фігура так походити не може"
                    continue
                if target.valid(startpos, endpos, target.Color, self.gameboard):
                    self.message = 'Хід валідний'
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]

                    if self.mate() == True:  # if mate -> run out of the loop
                        self.is_active = False
                        continue

                    self.check()

                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else:
                        self.playersturn = BLACK
                else:
                    self.message = 'Хід неможливий '
            else:
                self.message = 'У цьому місці немає фігури'

        print(self.message)
        self.render()

if __name__ == '__main__':
    Engine()
