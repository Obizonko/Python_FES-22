"""
Classes Board, Piece, and Game are implemented 
using the Singleton creational pattern.

The Singleton creational pattern is applied implicitly 
as we are not allowing multiple instances of 
Board and Piece classes to be created, and we are using 
a single instance of the Game class to manage the game state.
"""

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def place_piece(self, row, col, piece):
        if self.board[row][col] is None:
            self.board[row][col] = piece
            return True
        return False

    def remove_piece(self, row, col):
        if self.board[row][col] is not None:
            self.board[row][col] = None
            return True
        return False

    def display(self):
        for row in self.board:
            print(row)


class Piece:
    def __init__(self, color):
        self.color = color

    def display(self):
        print(f"Piece Color: {self.color}")


class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.pieces = {}

    def create_piece(self, piece_id, color):
        if piece_id not in self.pieces:
            piece = Piece(color)
            self.pieces[piece_id] = piece
            return piece
        return None

    def get_piece(self, piece_id):
        return self.pieces.get(piece_id, None)

    def place_piece(self, piece_id, row, col):
        piece = self.pieces.get(piece_id, None)
        if piece is not None:
            return self.board.place_piece(row, col, piece)
        return False

    def remove_piece(self, row, col):
        return self.board.remove_piece(row, col)

    def display_board(self):
        self.board.display()
