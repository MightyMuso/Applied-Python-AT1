from __future__ import annotations
from letterbox import Letterbox
from letter import Letter
from time import ctime


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.letterbox = Letterbox()
        self.letters = []

    def __repr__(self):
        return f"From {self.name} at {self.address}:"

    def read_letter_from_letterbox(self):
        """Reads the letters that are in the letterbox"""
        if self.letterbox.contains_letter():
            print(f"\nLetter read at {ctime()}\n")
            return self.letterbox.letterbox_letters

    def write_letter(self, message):
        """Creates an instance of a letter"""
        self.letters.append([self, message])
        # print("DEV :: LETTER WRITTEN")

    def post_letter(self, receiver: Person):
        for letter in self.letters:
            receiver.letterbox.set_letter(letter)
        receiver.letterbox.contains_letter()
        # print("DEV :: LETTER SENT")
