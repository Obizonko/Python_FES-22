import chess


if __name__ == '__main__':
    game = chess.Game()
    game.board.fill_random(show=True)
    game.play()

# test: b2b3, b7b6, c1a3, b8a6, a3e7
