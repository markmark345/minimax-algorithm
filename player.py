from msilib.schema import Class
import random
from turtle import pos

class Human:
    def __init__(self, marker):
        self.marker = marker
        self.type = "Human"

    def move(self, gi):
        while True:
            position = input("Your turn human: ")

            try:
                position = int(position)
            except:
                position = -1

            if position not in gi.get_free_positions():
                print("Can't move plase retry.")
            else:
                break

        gi.mark(self.marker, position)