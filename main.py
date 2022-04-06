import random
from shutil import move
import player
import minimax

class TicTacToe:
    def __int__(self):
        self.board = [' '] * 9
        self.lastmoves = []
        self.winner = None

    def display_board(self):
        print("   |   |   ")
        print("____|____|____")
        print(" %s | %s | %s " % (self.board[0], self.board[1], self.board[2]))
        print("____|____|____")
        print(" %s | %s | %s " % (self.board[3], self.board[4], self.board[5]))
        print("____|____|____")
        print(" %s | %s | %s " % (self.board[6], self.board[7], self.board[8]))
        print("____|____|____")
        print("   |   |   ")

    def mark(self, marker, pos):
        self.board[pos] = marker
        self.lastmoves.append(pos) 

    def revert_last_move(self):
        self.board[self.lastmoves.pop()] = ' '
        self.winner = None

    def avaliable_position(self):
        move = []
        for i, checkMove in enumerate(self.board) :
            if checkMove == ' ' :
                moves.append(i)
        return move

    def mark(self, marker, pos):
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def end_game(slef):
        win_positions = [(0,1,2), (3,4,5), (6,7,8), 
                        (0,3,6),(1,4,7),(2,5,8), 
                        (0,4,8), (2,4,6)]
        
        for i, j, k in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != ' ':
                self.winner = self.board[i]
                return True

        if ' ' not in self.board:
            self.winner = ' '
            return True
        return False


