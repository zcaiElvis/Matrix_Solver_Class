import unittest
from matrix import MatrixSolver


class Test_Matrix_Solver(unittest.TestCase):

    def setUpTest(self):
        self.ms = MatrixSolver()
        self.c = [[10,1,1],[1,2,7],[2,6,8]]
        self.d = [[3,3],[1,2]]

        self.uneven1 = [[1,2,3,4],[3,4,5,8]]
        self.uneven2 = [[1,2,3],[3,4,5],[5,6,7],[7,8,9]]
        self.uneven3 = [[1,2],[3,4],[5,6]]


    def test_iterationManager(self):

        self.setUpTest()

        resultc = self.ms.iterationManager(self.c)
        resultuneven1 = self.ms.iterationManager(self.uneven1)
        resultuneven2 = self.ms.iterationManager(self.uneven2)

        self.assertEqual(resultc, 2)
        self.assertEqual(resultuneven1, 1)
        self.assertEqual(resultuneven2, 2)


    def test_findSwapMax(self):

        self.setUpTest()

        resultc = self.ms.findSwapMax(self.c,2)
        newc = [[2,6,8],[1,2,7], [10,1,1]]

        resultuneven1 = self.ms.findSwapMax(self.uneven1,1)
        newuneven1 = [[3,4,5,8],[1,2,3,4]]

        resultuneven2 = self.ms.findSwapMax(self.uneven2,0)
        newuneven2 = [[7,8,9],[5,6,7],[3,4,5],[1,2,3]]

        resultuneven3 = self.ms.findSwapMax(self.uneven3,0)
        newuneven3 = [[5,6],[3,4],[1,2]]


        self.assertEqual(resultc, newc)
        self.assertEqual(resultuneven1, newuneven1)
        self.assertEqual(resultuneven3, newuneven3)


    def test_reduce_Pivot_Column(self):

        self.setUpTest()

        resultc = self.ms.reducePivotColumn(self.c, 0)
        newc = [[10,1,1],[0,-19,-69],[0,-29,-39]]

        resultd = self.ms.reducePivotColumn(self.d, 0)
        newd = [[3,3],[0,-3]]

        self.assertEqual(resultd, newd)
        self.assertAlmostEqual(resultc, newc)
