

class Letter:

    def __init__(self, sender, message: str):
        self.message = message
        self.sender = sender
        self.is_read = False

    #def __repr__(self):
        #return f"From {self.message}"
