from socket import AI_ADDRCONFIG

from minimax_Tic_tac_toe.main import mark


class Minimax:
    def __init__(self, marker):
        self.marker = marker
        self.type = "AI"

    def move(self, gi):
        move_position, score = self.maximized_move(gi)
        gi.mark(self.marker,move_position)

    def mix_move(self, gi):
        bestMove = None
        bestScore = None

        for move in gi.avaliable_position():
            gi.mark(self.marker, move)

            if gi.end_game()