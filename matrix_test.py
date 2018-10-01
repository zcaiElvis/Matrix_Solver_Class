import unittest
from matrix import MatrixSolver


class Test_Matrix_Solver(unittest.TestCase):

    def setUpTest(self):
        self.ms = MatrixSolver()

        self.a = [[1,2,2],[2,6,2],[3,5,5]]
        self.b = [[1,2,2],[3,4,5]]

        self.c = [[2,3,4],[5,7,3],[2,6,5],[3,4,8]]
        self.d = [[1,2,3,4],[4,5,7,2],[2,8,7,1]]


    def test_UpperTriangularFunction(self):

        self.setUpTest()

        resulta = self.ms.upperTriangularMatrix(self.a)
        resultb = self.ms.upperTriangularMatrix(self.b)
        resultc = self.ms.upperTriangularMatrix(self.c)
        resultd = self.ms.upperTriangularMatrix(self.d)

        checka = [[3, 5, 5], [0.0, -1.0, -1.0], [0.0, 0.0, -1.5]]
        checkb = [[3, 4, 5], [0.0, -2.0, -1.0]]
        checkc = [[5, 7, 3], [0.0, 0.33333333333333304, -10.333333333333334], [0.0, 0.0, -10.729166666666666], [0.0, 0.0, -14.999999999999996]]
        checkd = [[4, 5, 7, 2], [0.0, -3.0, -5.0, -14.0], [0.0, 0.0, -3.090909090909091, -14.0]]

        self.assertAlmostEqual(resulta, checka)
        self.assertAlmostEqual(resultb, checkb)
        self.assertAlmostEqual(resultc, checkc)
        self.assertAlmostEqual(resultd, checkd)
