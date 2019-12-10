class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self._board = []
        for _ in range(y):
            self._board.append(['-' for i in range(x)])

    def __str__(self):
        stringified = ""

        for _ in range(self.x):
            stringified += '--'
        stringified += '\n'
        for y in range(self.y):
            stringified += '| '
            for x in range(self.x):
                stringified += self._board[y][x] + ' '
            stringified += '|\n'

        return stringified
