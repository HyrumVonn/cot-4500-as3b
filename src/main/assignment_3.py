#Hyrum VonNiederhausern
import copy

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

def GaussianElimination(matrix):
    #order our matrix, so that the first row starts on 1
    matrixModified = OrderMatrix(matrix)

    ilength = len(matrixModified[0])

    #set all values with j's higher than i to 0
    for i in range(ilength):
        jlength = len(matrixModified)
        for j in range(i + 1, jlength):
            #Grab the row above it (j - 1). 
            rowCurrent = matrixModified[j]
            rowPrev = matrixModified[j - 1]

            if(rowPrev[i] == 0):
                #if we would divide by 0, grab the next row before that, until we do not
                #warning; potential to still fault
                tempJ = j - 1
                while((rowPrev[i] == 0) and (tempJ >= 0)):
                    tempJ = tempJ - 1
                    rowPrev = matrixModified[tempJ]

                if(rowPrev[i] == 0):
                    print(f"Error! In matrix {matrixModified}, no suitable coefficient to nullify element {i},{j} ({matrixModified[i][j]})")

            coeff = - rowCurrent[i] / rowPrev[i]

            matrixModified[j] = MatrixAddRows(rowCurrent, rowPrev, coeff)

    result = LinearSolveTriangleMatrix(matrixModified)

    print(result)

def LUFactorization(matrix):
    return 0

def DiagonallyDominant(matrix):
    return True

def PositiveDefinite(matrix):
    return True


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
