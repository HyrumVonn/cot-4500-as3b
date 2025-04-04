#Hyrum VonNiederhausern
import copy
import numpy


#Problem 1
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

    #A general number to be used; length of the array of variables that we output; number of rows 
    #in the input matrix
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

        #skipping over the sum column, add up each variable we've already calculated with its corre-
        #-sponding coefficient on this row, and remove that from sum
        for j in range(1, i + 1):
            #j is a bottom up indexer when considering the columns in our given row
            #j is also a top down indexer when it comes to accessing calculated variables  
            #(hence, why we subtract it from number of Xs to get a given variable)
            value = result[(numXs - 1) - (j - 1)] * row[j]
            sum = sum - value
        
        #then, what remains of the sum, divide it by the furthermost coefficient in the row, and
        #that must be the variable for this row; save it into our array of variables
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
            resultLower[j][i] = -coeff

    return resultUpper, resultLower

def GaussianElimination(matrix):
    matrixModified = OrderMatrix(matrix)
    
    matrixModified, lowTriangleMat = DecomposeToTriangleMatrices(matrixModified)
    
    result = LinearSolveTriangleMatrix(matrixModified)

    print(numpy.array(result))


#Problem 2
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


    print(numpy.array(LMat))
    print()
    print(numpy.array(UMat))
    print()

def SumRowMagnitude(row):
    result = 0

    length = len(row)

    for i in range(length):
        result = result + abs(row[i])

    return result

def DiagonallyDominant(matrix):
    length = len(matrix)
    result = True

    for i in range(length):
        mag = abs(matrix[i][i])

        #must subtract the magnitude of the diagonal
        #from the total sum of magnitudes in the row
        if (mag < (SumRowMagnitude(matrix[i]) - mag)):
            #if all are >=, it is true. Therefore, if
            #any are <, it is false
            result = False

    print(result)


def InvertMatrix(matrix):
    result = []

    length = len(matrix)

    for i in range(length):
        row = []
        for j in range(length):
            row.append(0)
        result.append(row)

    for i in range(length):
        for j in range(length):
            result[i][j] = matrix[j][i]

    return result

def PositiveDeterminants(matrix):
    #make submatrices for each square, until you reach total
    #if any of them are not, positive, then return false
    length = len(matrix)

    for size in range(length):
        submatrix = []
        for i in range(size + 1):
            row = []
            for j in range(size + 1):
                row.append(matrix[i][j])
            submatrix.append(row)
        
        Det = Determinant(submatrix)

        if(Det <= 0):
            return False

    return True

def PositiveDefinite(matrix):
    result = True

    inverted = InvertMatrix(matrix)

    if(not(numpy.array_equal(matrix, inverted))):
        result = False

    if(not PositiveDeterminants(inverted)):
        result = False

    print(result)


GaussianElimination([[2,-1,1,6],
                     [1,3,1,0],
                     [-1,5,4,-3]])

print()

LUFactorization([[1,1,0,3],
                 [2,1,-1,1],
                 [3,-1,-1,2],
                 [-1,2,3,-1]])

print()

DiagonallyDominant([[9,0,5,2,1],
                    [3,9,1,2,1],
                    [0,1,7,2,3],
                    [4,2,3,12,2],
                    [3,2,4,0,8]])

print()

PositiveDefinite([[2,2,1],
                  [2,3,0],
                  [1,0,2]])
