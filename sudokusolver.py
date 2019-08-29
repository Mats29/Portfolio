import time
import numpy as np
from copy import deepcopy
'''
Solves sudoku grids recursively
'''
def convert(string):
    '''
    Takes an input string of the rows of a sudoku and converts it to a 9x9 numpy array
    '''
    arr=[]
    vector=[]
    for i in range(len(string)):
        vector.append(int(string[i]))
        if i%9 == 8: #collects the rows of 9 inputs
            arr.append(vector)
            vector=[]
    return np.array(arr)
def entry(a, b, grid):
    '''
    Collects a specific entry within the sudoku
    '''
    return grid[a-1,b-1]
def ispossible(a,b,n,grid):
    '''
    Checks if a specific number is possible at a given position
    '''
    temp=entry(a, b, grid)
    grid[a-1, b-1]=0
    for i in range(1,10):
        if n == entry(a, i, grid): #checks for matches within the row
            grid[a-1, b-1]=temp
            return False
        elif n == entry(i, b, grid): #checks for matches down the column
            grid[a-1, b-1]=temp
            return False
    r=(a-1)//3
    s=(b-1)//3
    for i in range(1,4): #used to check for matches within the 3x3 square
        for j in range(1,4):
            if n == entry(3*r+i, 3*s+j, grid):
                grid[a-1, b-1]=temp
                return False
    grid[a-1, b-1]=temp
    return True
def computepossibilities(a,b,grid):
    '''
    Creates a list of all posible entries at a given position
    '''
    nlist=[]
    for n in range(1, 10):
        if ispossible(a,b,n, grid) == True:
            nlist.append(n)
    return np.array(nlist)
def Set(a, b, n, grid):
    if entry(a, b, grid) != 0 or ispossible(a, b, n, grid) == False:
        return False
    else:
        grid[a-1, b-1] = n
    return True
def singletons(grid):
    '''
    Runs the function computepossibilities and changes the value in the sudoku grid when there is only one possible option
    '''
    m=False
    for i in range(1,10):
        for j in range(1,10):
            if entry(i, j, grid) == 0 and len(computepossibilities(i, j, grid)) == 1:
                grid[i-1, j-1] = computepossibilities(i, j, grid)[0]
                m=True
    return m
def simplesolve(grid):
    '''
    Runs the singletons function until the sudoku is finished
    '''
    while singletons(grid):
        pass
def issolved(grid):
    '''
    Verifies that all entriess are non-zero
    '''
    for i in range(1,10):
        for j in range(1,10):
            if grid[i-1, j-1] == 0:
                return False
    return True
def issolvable(grid):
    '''
    Checks all entries that have not been filled out to see if there are many
    remaining possibilities
    '''
    for i in range(1,10):
        for j in range(1,10):
            if ((grid[i-1, j-1] == 0) and len(computepossibilities(i,j,grid))==0):
                return False
    return True
def solve(grid):
    '''
    Solves the sudoku by piecing together the above functions
    '''
    simplesolve(grid)
    if issolved(grid) == True:
        return grid
    possibities=[1,1,1,1,1,1,1,1,1,1]
    A=0
    B=0
    if issolvable(grid) == True:
        for i in range(1,10):
            for j in range(1,10):
                if grid[i-1, j-1] == 0 and len(possibities) > len(computepossibilities(i,j,grid)):
                    A=i
                    B=j
                    possibilities = computepossibilities(A,B,grid)
        for k in possibilities:
            newgrid = deepcopy(grid)
            Set(A, B, k, newgrid)
            if issolvable(grid) == True:
                newgrid=solve(newgrid)
                if type(newgrid) == np.ndarray:
                    return newgrid
                else:
                    continue
    return False
if __name__=="__main__":
    A = time.time()
    string = '003000900020904060700050003010305080006080300050209070500010008080703010009000400'
    a = '980100000501000000067089000300206400004000800005708006000350260000000301000002045'
    b = '010702080300050001006000700600070004090423060400080009003000900800040002050607040'
    c = '903050400060008010100000007000070090300809005050060000200000006080400030006030801'
    d = '400030000000600800000000001000050090080000600070200000000102700503000040900000000'
    e = '708000300000201000500000000040000026300080000000100090090600004000070500000000000'
    f = '708000300000601000500000000040000026300080000000100090090200004000070500000000000'
    g = '307040000000000091800000000400000700000160000000250000000000380090000500020600000'
    h = '500700600003800000000000200620400000000000091700000000000035080400000100000090000'
    i = '400700600003800000000000200620500000000000091700000000000043080500000100000090000'
    j = '040010200000009070010000000000430600800000050000200000705008000000600300900000000'
    grid=convert(string)
    print(solve(grid))
    B = time.time()
    print(abs(A-B))
