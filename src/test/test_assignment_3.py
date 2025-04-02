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

def Lin

def GaussianElimination(matrix):
    print(matrix)

    matrixModified = OrderMatrix(matrix)
    print(matrixModified)

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
            #the coefficient will be whatever it takes for matrix[j-1][i] 

    print(matrixModified)
    print()

GaussianElimination(matrix=[[2, -1, 7],[-1, 1, 1]])

GaussianElimination(matrix=[[1, 2, 1, 7],[2, -1, 1, 4],[3, 1, 1, 10]])

GaussianElimination(matrix=[[2, 1, 2, 18],[1, -1, 2, 9],[1, 2, -1, 6]])
