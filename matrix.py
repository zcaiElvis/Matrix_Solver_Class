from decimal import *
from fractions import *


class MatrixSolver:

    def isValidMatrix(self, A):
        s = len(A[0])
        for x in range(0,len(A)):
            if not len(A[x]) == s:
                print("Matrix not valid: all rows have to be the same size")
                return
        print("Matrix valid. Matrix is {} by {}".format(len(A[0]), len(A)))


    def upperTriangularMatrix(self, A):
        self.isValidMatrix(A)
        numit = self.iterationManager(A)
        for x in (0, numit):
            self.startPivoting(A,x)



    def startPivoting(self,A,x):
        self.findSwapMax(A,x)
        self.reducePivotColumn(A,x)



    def findSwapMax(self, A, x):
        numit = self.iterationManager(A)
        maxRowNumber = x

        for y in range(0,len(A)):
            print(A[y][x], A[maxRowNumber][x])
            if A[y][x] > A[maxRowNumber][x]:
                maxRowNumber = y

        tmp = A[0]
        A[0] = A[maxRowNumber]
        A[maxRowNumber] = tmp

        return A;


    def reducePivotColumn(self,A,x):
        numit = self.iterationManager(A)
        pivotRow = x
        pivot = A[x][x]

        for m in range(1, numit+1):
            reduceTerm = A[m][x]
            if reduceTerm != 0:
                ratio = pivot/reduceTerm
            l = A[m]
            A[m] = [c - a * ratio for c,a in zip(A[pivotRow],l)]

        return A


    def iterationManager(self,A):
        numRow = len(A)
        numCol = len(A[0])
        return min(numRow,numCol)-1













a  = MatrixSolver()
someMatrix = [[1,2]]
somearray=[1,2,3]




c=[[10,1,1],[1,2,7],[2,6,8]]


print(c)
a.findSwapMax(c,0)
print(c)
