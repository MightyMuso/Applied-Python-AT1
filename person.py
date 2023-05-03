from __future__ import annotations
from letterbox import Letterbox
from post_office import PostOffice
from letter import Letter
from encyrpted_letter import EncryptedLetter
from time import ctime


class Person:

    def __init__(self, name, address, encryption_key=None):
        self.name = name
        self.address = address
        self.letterbox = Letterbox()
        self.encryption_key = encryption_key
        
    # def secret(self, key):
        # self.encryption_key = key

    def __repr__(self):
        return f"From {self.name} at {self.address}, sent {ctime()}:"

    def read_letter(self):
        """Reads the letters that are in the letterbox"""
        if self.letterbox.has_letters():
            while self.letterbox.has_letters():
                letter = self.letterbox.get_letters()
                if isinstance(letter, EncryptedLetter):
                    letter.decrypt_message(self.encryption_key)
                    print(f"Letters read by {self.name} at {ctime()}")
                if isinstance(letter, Letter):
                    letter.read_letter()
                    print(f"Letters read by {self.name} at {ctime()}")
        else:
            print(f"\n{self.name} has no new letters\n")
        return self.letterbox.letters

    def write_letter(self, receiver: Person, message: str, post_office: PostOffice):
        """Creates an instance of a letter"""
        letter = Letter(self, receiver, message)
        encrypted_letter = EncryptedLetter(self, receiver, message, self.encryption_key)
        if encrypted_letter.sender is receiver:
            raise Exception("Cannot send self a letter")
        elif isinstance(letter, EncryptedLetter):
            post_office.set_letters(encrypted_letter)
        elif isinstance(letter, Letter):
            post_office.set_letters(letter)


