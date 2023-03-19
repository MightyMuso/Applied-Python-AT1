# from __future__ import annotations


class Letter:

    def __init__(self, sender, message: str, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver
        self.is_read = False
