


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
        for x in range(0, len(A[0])-1):
            self.startPivoting(A,x)

        return A



    def startPivoting(self,A,x):
        print(" here in startPivoting" + str(x))
        self.findSwapMax(A,x)
        self.reducePivotColumn(A,x)

        return A



    def findSwapMax(self, A, x):
        maxRowNumber = x

        for y in range(x,len(A)):
            if A[y][x] > A[maxRowNumber][x]:
                maxRowNumber = y

        tmp = A[x]
        A[x] = A[maxRowNumber]
        A[maxRowNumber] = tmp

        return A;


    def reducePivotColumn(self,A,x):
        pivotRow = x
        pivot = A[x][x]

        for m in range(x+1, len(A)):
            # print("m value is " + str(m))
            reduceTerm = A[m][x]
            if reduceTerm != 0:
                ratio = pivot/reduceTerm
            l = A[m]
            A[m] = [c - a * ratio for c,a in zip(A[pivotRow],l)]

        print("new A" + str(A))

        return A







# a = MatrixSolver()


e = [[1,2,2],[2,6,2],[3,3,5]]
f = [[1,2,2],[2,6,2],[3,5,5]]
f1= [[1,2,2],[2,6,2],[3,5,5]]
g = [[1,2,2],[3,4,5]]

w = [[2,3,4],[5,7,3],[2,6,5],[3,4,8]]
q = [[1,2,3,4],[4,5,7,2],[2,8,7,1]]

# dnew = [[3,4],[0,-2],[0, -5]]
# print("--------")
# print(a.startPivoting(d,0))
# print(a.startPivoting(d,1))

# print(a.startPivoting(e,0))
# print("second start here")
# print(a.findSwapMax(e,1))
# print(a.reducePivotColumn(e,1))

# print(a.startPivoting(f,0))
# print(a.startPivoting(f,1))
# print(a.upperTriangularMatrix(g))
# print(a.upperTriangularMatrix(f1))
# print("-------------------------------------------")
# print(a.upperTriangularMatrix(g))
# print(a.upperTriangularMatrix(w))
# print(a.upperTriangularMatrix(q))


a = MatrixSolver()

# print(a.upperTriangularMatrix(f))
# print(a.upperTriangularMatrix(g))
print(a.upperTriangularMatrix(w))
# print(a.upperTriangularMatrix(q))
