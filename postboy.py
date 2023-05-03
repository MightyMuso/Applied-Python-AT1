from person import Person
from post_office import PostOffice
from letter import Letter
from time import ctime


class Postboy(Person):
    def __init__(self, name: str, post_office: PostOffice):
        super().__init__(name, address=PostOffice().address)
        self.letters = []
        self.post_office = post_office

    def get_letters(self):
        if self.post_office.has_letters():
            self.letters.extend(self.post_office.get_letters())
            # Extend adds to the list instead of overwriting it
            print(f"Letters collected by Postboy {self.name} at {ctime()}")
        else:
            print("No letters")

    def has_letters(self):
        return bool(self.letters)

    def deliver_letters(self):
        if self.has_letters():
            for letter in self.letters:
                recipient = letter.receiver
                recipient.letterbox.set_letters(letter)
                print(f"Letters delivered by Postboy {self.name} at {ctime()}")







