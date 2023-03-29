

class Letterbox:

    def __init__(self):
        self.letters = []

    def has_letters(self):
        return bool(self.letters)
    # Returns ture is list is populated, returns false if not

    def get_letters(self):
        if not self.has_letters():
            raise IndexError("No letters")
            # Raises an error and stops the program
        return self.letters.pop()

    def set_letters(self, letter):
        self.letters.append(letter)
