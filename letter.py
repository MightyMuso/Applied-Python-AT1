

class Letter:

    def __init__(self, sender, receiver, message: str):
        self._message = message
        self.sender = sender
        self.receiver = receiver
        self._read = False

    def __repr__(self):
        return f"From {self.sender.name} to {self.receiver.name}: {self._message}"

    def is_read(self):
        return self._read

    def read_letter(self):
        self._read = True
        return self._message
