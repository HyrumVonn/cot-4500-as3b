import numpy
import copy
#Gaussian elimination and backward substitution 
#2  -1  1   6
#1  3   1   0
#-1 5   4   -3

#def ClearMatrix(matrixIn):
    # Go through every row that's got y's below the current x, and perform a
    # 
def OrderMatrix(matrixIn):
    result = copy.deepcopy(matrixIn)

    jlength = len(result)

    for i in range(jlength):
        if(result[i][0] == 1):
            #if you find a row that begins with a 1, set that as the first row
            temp = result[0]
            result[0] = result[i]
            result[i] = temp
            break
        else:
            #if we have reached the end, then simply make the first row so that it begins with 1
            if((i + 1) == jlength):
                #divide the first row by its first constant
                origValue = result[0][0]
                for j in range(len(result[0])):
                    result[0][j] = (result[0][j]) / origValue

    #output the fixed array
    return result 

def MatrixAddRows(RowA, RowB, CoefficientB):
    result = []

    for j in range(len(RowA)):
        result.append(RowA[j] + (CoefficientB * RowB[j]))

    return result

def LinearSolveTriangleMatrix(matrix):
    result = []

    for i in range(len(matrix)):
        result.append(0)

    numXs = len(result)

    #start at the bottom of the matrix: for 
    # 1 2 |3
    # 0 1 |2
    # we want to consider it starting from row
    # 0 1 |2
    # 1 2 |3
    mTemp = list(reversed(matrix))

    for i in range(numXs):
        # Within each row, consider from the end to the beginning, first. So, previous example
        # matrix will now be 
        # 2| 1 0
        # 3| 2 1
        row = list(reversed(mTemp[i]))
        #get the total that this row must sum to
        sum = row[0]

        for j in range(1, i + 1):
            value = result[(numXs - 1) - (j - 1)] * row[j]
            sum = sum - value
        
        result[(numXs - 1) - i] = sum / row[i + 1]

    return result

def DecomposeToTriangleMatrices(matrix):
    resultUpper = copy.deepcopy(matrix)
    ilength = len(resultUpper[0])

    resultLower = numpy.identity(len(matrix))

    #set all values with j's higher than i to 0
    for i in range(ilength):
        jlength = len(resultUpper)
        for j in range(i + 1, jlength):
            #Grab the row above it (j - 1). 
            rowCurrent = resultUpper[j]
            rowPrev = resultUpper[j - 1]

            if(rowPrev[i] == 0):
                #if we would divide by 0, grab the next row before that, until we do not
                #warning; potential to still fault
                tempJ = j - 1
                while((rowPrev[i] == 0) and (tempJ >= 0)):
                    tempJ = tempJ - 1
                    rowPrev = resultUpper[tempJ]

                if(rowPrev[i] == 0):
                    print(f"Error! In matrix {matrix}, no suitable coefficient to nullify element {i},{j} ({resultUpper[i][j]})")

            coeff = - rowCurrent[i] / rowPrev[i]

            resultUpper[j] = MatrixAddRows(rowCurrent, rowPrev, coeff)

    return resultUpper, resultLower

def GaussianElimination(matrix):
    print(matrix)

    matrixModified = OrderMatrix(matrix)
    print(matrixModified)

    matrixModified, lowTriangleMat = DecomposeToTriangleMatrices(matrixModified)
    print(matrixModified)

    result = LinearSolveTriangleMatrix(matrixModified)

    print(result)


def Determinant(matrix):
    length = len(matrix)
    #base case (when only one element remains)
    if(length == 1):
        return matrix[0][0]
    
    #when a 2x2 matrix remains
    if(length == 2):
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    sum = 0
    topRow = matrix[0]
    for coeff in range(length):
        subMatrix = []
        #coefficients will always be the top row, so can safely start the submatrix on row 1
        for i in range(1, length):
            rowMatrix = []
            for j in range(length):
                if (j == coeff):
                    continue
                rowMatrix.append(matrix[i][j])

            subMatrix.append(rowMatrix)
        
        print(f"{pow(-1, coeff)} * {topRow[coeff]} * {subMatrix}")
        sum = sum + (pow(-1, coeff)) * topRow[coeff] * Determinant(subMatrix)

    return sum


def LUFactorization(matrix):
    determinant = Determinant(matrix)
    print(determinant)
    print()
    
    if(determinant == 0):
        print("Error: determinant is 0, cannot decompose Matrix")
        return
    
    UMat, LMat = DecomposeToTriangleMatrices(matrix)
    print(LMat)
    print()
    print(UMat)
    print()

GaussianElimination(matrix=[[2, -1, 7],[-1, 1, 1]])
print()

GaussianElimination(matrix=[[1, 2, 1, 7],[2, -1, 1, 4],[3, 1, 1, 10]])
print()

GaussianElimination(matrix=[[2, 1, 2, 18],[1, -1, 2, 9],[1, 2, -1, 6]])
print()

GaussianElimination([[2,-1,1,6],
                     [1,3,1,0],
                     [-1,5,4,-3]])
print()

GaussianElimination([[2,1,2,18],
                     [1,-1,2,9],
                     [1,2,-1,6]])

# LUFactorization([[2,    -1,     3,  0],
#                  [4,    -2,     7,  0],
#                  [-3,   -4,     1,  5],
#                  [6,    -6,     8,  0]])
# print("\n\n")

# LUFactorization([[1,1,0,3],
#                  [2,1,-1,1],
#                  [3,-1,-1,2],
#                  [-1,2,3,-1]])
# print("\n\n")

# LUFactorization([[1,0,4,-6],
#                 [2,5,0,3],
#                 [-1,2,3,5],
#                 [2,1,-2,3]])
