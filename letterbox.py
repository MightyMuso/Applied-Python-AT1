from letter import Letter


class Letterbox:

    def __init__(self):
        self.letterbox_letters = []

    #def update_letter(self, letter: Letter):
        #self.letters = letter

    def contains_letter(self):
        if len(self.letterbox_letters) > 0:
            return self.letterbox_letters

    def set_letter(self, letter):
        self.letterbox_letters.append(letter)
