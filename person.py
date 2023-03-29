from __future__ import annotations
from letterbox import Letterbox
from letter import Letter
from time import ctime


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.letterbox = Letterbox()

    def __repr__(self):
        return f"From {self.name} at {self.address}, sent {ctime()}:"

    def read_letter(self):
        """Reads the letters that are in the letterbox"""
        if self.letterbox.has_letters():
            while self.letterbox.has_letters():
                letter = self.letterbox.get_letters()
                letter.read_letter()
            print(f"\nLetters read at {ctime()}\n")
        else:
            print("No new letters\n")
        return self.letterbox.letters

    def write_letter(self, receiver, message):
        """Creates an instance of a letter"""
        letter = Letter(self, receiver, message)
        if letter.sender == receiver:
            raise Exception("Cannot send self a letter")
        else:
            receiver.letterbox.set_letters(letter)
        # print("DEV :: LETTER WRITTEN")

    # def post_letter(self, receiver: Person):
    # for letter in self.letters:
    # receiver.letterbox.set_letter(letter)
    # receiver.letterbox.has_letters()
    # print("DEV :: LETTER SENT")
