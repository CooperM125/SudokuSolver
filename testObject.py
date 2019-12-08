import unittest
import object

'''
test the objects to make sure they have the correct
properties and functions.
'''


class testObjects(unittest.TestCase):
    def testSquare(self):
        square = object.Square(1)
        resultNum = square.number
        resultList = square.posibleNumbers
        expectedNum = 1
        expectedList = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(resultNum, expectedNum)
        self.assertEqual(resultList, expectedList)

    def testRemovePosNum(self):
        numbers = [2, 4, 0, 9, 8, 1, 0, 0, 0]
        row = []
        solver = object.Solver()
        for number in numbers:
            row.append(object.Square(number))
        solver.solveRow(row)
        expectedList = [3, 5, 6, 7]
        resultList = row[8].posibleNumbers
        self.assertEqual(resultList, expectedList)

    # TODO: def testMakeRow(self):
    # TODO: def testRowSolved(self):


if __name__ == '__main__':
    unittest.main()
