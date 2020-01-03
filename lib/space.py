class Space:
    def __init__(self):
        self.filled = False

    def is_filled(self):
        return self.filled

    def fill(self):
        self.filled = True

    def empty(self):
        self.filled = False
