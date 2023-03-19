from letterbox import Letterbox
from letter import Letter

# GLOBAL NOTES
# .letter refers to the written letter
# .letterbox.letter refers to the received letter from the letterbox


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.letterbox = Letterbox()
        self.letter = None
        # None is just a placeholder, so it can be used later to check for letter

    def read_letter_from_letterbox(self):
        """Reads the letter that is in the letterbox"""
        if self.letterbox.letter is not None:
            # The letter is now a Letter object, assuming post_letter has already occurred
            self.letterbox.letter.is_read = True
            self.letterbox.has_letter = False

    def write_letter(self, message, receiver):
        """Creates an instance of a letter if the letter from the letterbox has been read"""
        if self.letterbox.has_letter is False:
            self.letter = Letter(self, message, receiver)
            # self as an argument refers to the Person writing the letter (Bob or Ophelia)

    def post_letter(self, receiver):
        """Sends the letter instance from write_letter to the receiver's letterbox"""
        if receiver.letterbox.has_letter is False:
            receiver.letterbox.get_letter(self.letter)
            # Receiver's letterbox gets the letter from the sender
            receiver.letterbox.has_letter = True


if __name__ == "__main__":
    bob = Person("Bob", 123)
    ophelia = Person("Ophelia", 456)

    bob.read_letter_from_letterbox()
    bob.write_letter("g'day", ophelia)
    bob.post_letter(ophelia)
    print(ophelia.letterbox.letter.message)

    ophelia.read_letter_from_letterbox()
    ophelia.write_letter("'sup", bob)
    ophelia.post_letter(bob)
    print(bob.letterbox.letter.message)
