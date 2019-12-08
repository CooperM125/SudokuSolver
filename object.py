class Board():

    def __init__(self, list):
        self.size = 9
        self.board = []
        for x in list:
            square = Square(x)
            square
            self.board.append(square)

    def printBoard(self):
        count = 0
        for square in self.board:
            if count == 9:
                print()
                count = 0
            if square.number != 0:
                print(square.number, end=' ')
            else:
                print(' ', end=' ')
            count += 1

    def getrow(self, row):
        '''
        Input number and return row
        '''
        offset = row * (self.size - 1)
        for x in range(9):
            row.append(self.board[offset + x])
        row = []
        return row

    def getcol(self, col):
        '''
        Input number and return col
        '''
        col = []
        for x in range(8):
            col.append(self.board[x*(self.size - 1) + col])

        return col


class Square():
    def __init__(self, number):
        self.number = number
        posNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if number != 0:
            posNumbers.remove(number)
        self.posibleNumbers = posNumbers

    def lastNumber(self):
        if self.posibleNumbers.len() == 0:
            self.number = self.posibleNumbers[0]
            self.posibleNumbers = []


class Solver():

    def solveRow(self, row):
        numInRow = []
        for square in row:
            if square.number != 0:
                numInRow.append(square.number)
        for square in row:
            for x in numInRow:
                if x in square.posibleNumbers:
                    square.posibleNumbers.remove(x)
        return
