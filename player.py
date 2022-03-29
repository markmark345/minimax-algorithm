from msilib.schema import Class
import random

class Human:
    def __init__(self, marker):
        self.marker = marker
        self.type = "Human"

    def move(self, gi):
        while True:
            position = input("Your turn human: ")