class Tile:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ' '
        self.isFlipped = False
        self.isFlagged = False
        self.isMarked = False
        self.clicks = 0

    def flip(self):
        self.isFlipped = True

    def isMine(self):
        return self.value == '*'

    def isEmpty(self):
        return self.value == ' '

    def __str__(self):
        if (self.isFlipped):
            if (self.isMine()): 
                return "*"
            else:
                return self.value
        else:
            if (self.isFlagged):
                return "!"
            elif (self.isMarked):
                return "?"
            else:
                return "#"
