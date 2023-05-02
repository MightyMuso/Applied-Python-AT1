from letter import Letter


class EncryptedLetter(Letter):

    def __init__(self, sender, receiver, message, key: int):
        message = EncryptedLetter.encrypt_message(message, key)
        super().__init__(sender, receiver, message)

    @staticmethod  # Static methods can be called without creating an object or instance
    def encrypt_message(message, key):
        encrypted_message = []
        for char in message:
            shifted_char = ord(char) + key  # ord gets a numerical value of each string character
            encrypted_message.append(chr(shifted_char))
        return "".join(encrypted_message)  # Concatenates empty string with list contents

    def decrypt_message(self, key):
        return EncryptedLetter.encrypt_message(self.read_letter(), -key)


if __name__ == "__main__":
    letter = EncryptedLetter("x", "y", "hello", 5)
    print(letter.read_letter())
    print(letter.decrypt_message(5))


