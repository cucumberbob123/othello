class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self._board = []
        for _ in range(y):
            self._board.append(['-' for i in range(x)])

    def place(self, x, y, piece):
        if x > self.x or y > self.y or x <= 0 or y <= 0:
            raise PlacementError("invalid coordinates")

        self._board[self.y - y][x - 1] = piece
        self.update(x, y, piece)

    def update(self, x, y, piece):
        # TODO modularization and skip if multiple of same color in a row
        # NB: this doesn't really affect functionality, but it makes more sense
        distance = 0
        direction = ""

        # Check upwards
        for i in range(y, self.y + 1):
            if self.y - i == self.y - y:
                continue

            if self._board[self.y - i][x-1] == piece:
                newDistance = abs(i - y) - 1
                if newDistance > distance:
                    foundX = x - 1
                    foundY = i - y
                    distance = newDistance
                    direction = "u"

        # Check downwards
        for i in range(y, 0, -1):
            if self.y - i == self.y - y:
                continue

            if self._board[self.y - i][x-1] == piece:
                newDistance = abs(i - y) - 1
                if newDistance > distance:
                    foundX = x - 1
                    foundY = y - i
                    distance = newDistance
                    direction = "d"

        if distance == 0:
            return False

        print(f"{distance=}")

        print(f"{foundX=} {foundY=} {direction=}")
        self.replace(x, y, distance, direction, piece)

    def replace(self, x, y, distance, direction, piece):
        if direction == 'u':
            for i in range(y + 1, y + 1 + distance):
                self._board[self.y-i][x - 1] = piece
            return

        if direction == 'd':
            for i in range(y - distance, y):
                self ._board[self.y-i][x - 1] = piece
            return

    def toString(self):
        stringified = ""

        line = ""
        for _ in range(3 + (self.x*2)):
            line += '-'
        line += '\n'

        stringified += line

        for y in range(self.y):
            stringified += '| '
            for x in range(self.x):
                stringified += self._board[y][x] + ' '
            stringified += '|\n'

        stringified += line

        return stringified


class PlacementError(Exception):
    pass
