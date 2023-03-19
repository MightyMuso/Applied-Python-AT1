from letter import Letter


class Letterbox:

    def __init__(self):
        self.has_letter = False
        self.letter = None

    def contains_letter(self):
        return self.has_letter

    def get_letter(self, letter: Letter):
        self.letter = letter
