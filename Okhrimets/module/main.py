from figurines import *


class Board:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]

    def get_piece(self, x, y):
        piece_str = self.board[x][y]
        if piece_str is None:
            return None
        color = 'white' if piece_str.isupper() else 'black'
        piece_type = piece_str.lower()
        return Piece(color, piece_type)

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece(start_pos[0], start_pos[1])
        self.board[start_pos[0]][start_pos[1]] = None
        self.board[end_pos[0]][end_pos[1]] = piece

    def algebraic_to_numeric(self, pos):
        file, rank = pos[0], int(pos[1])
        x, y = rank - 1, ord(file) - ord('a')
        return x, y

    def display_board(self):
        print('   a b c d e f g h')
        print('  +-----------------+')
        for i, row in enumerate(self.board):
            rank = 8 - i
            row_str = str(rank) + ' | '
            for piece in row:
                if piece is None:
                    row_str += '. '
                else:
                    row_str += str(piece) + ' '
            row_str += '| ' + str(rank)
            print(row_str)
        print('  +-----------------+')
        print('   a b c d e f g h')


class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 'white')
        self.player2 = Player(player2_name, 'black')
        self.current_player = self.player1
        self.board = Board()

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def display_board(self):
        for row in self.board.board:
            print(str(row))

    def play(self):
        while True:
            print(self.board)
            print(f"It's {self.current_player.color}'s turn.")
            start_pos = input("Enter the starting position (e.g. 'e2'): ")
            end_pos = input("Enter the ending position (e.g. 'e4'): ")
            try:
                start_pos = self.board.algebraic_to_numeric(start_pos)
                end_pos = self.board.algebraic_to_numeric(end_pos)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            piece = self.board.get_piece(*start_pos)
            if piece is None:
                print("There is no piece at that position. Please try again.")
                continue
            if piece.color != self.current_player.color:
                print("That piece belongs to the other player. Please try again.")
                continue
            if not piece.is_valid_move(start_pos, end_pos, self.board):
                print("Invalid move. Please try again.")
                continue
            self.board.move_piece(start_pos, end_pos)
            self.board.display_board()
            self.change_player()


if __name__ == "__main__":
    game = Game("Alice", "Bob")
    game.play()
