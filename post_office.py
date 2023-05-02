from __future__ import annotations
from letter import Letter


class PostOffice:

    def __init__(self, address: str = "Big Boy Post"):
        self.address = address
        self.letters: list[Letter] = []

    def has_letters(self):
        return bool(self.letters)

    def get_letters(self):
        if not self.has_letters():
            raise IndexError("No letters")
            # Raises an error and stops the program
        while self.letters:
            yield self.letters.pop()
            # Yield pops off (removes) all items in the list while simultaneously returning them

    def set_letters(self, letter: Letter):
        self.letters.append(letter)



