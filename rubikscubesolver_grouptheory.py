import random
import time
'''
I used group theory to solve the cube, the squares on the faces of the cube
were each assigned a number and each square is part of a group, the operation
on the group being a spin on the cube. Below are the possible moves on each
face of the cube
'''
Right = [[2,18,23,7],[3,10,22,15],[6,14,19,11],[26,37,46,35],[30,34,42,38]]
Up = [[12, 9, 10, 11], [7, 8, 5, 6], [31, 32, 29,30], [25, 26, 27, 28], [1, 2, 3, 4]]
Front = [[3, 19, 24, 8], [4, 11, 23, 16], [27, 38, 47, 36], [7, 15, 20,12], [31, 35, 43, 39]]
Left = [[1, 12, 24, 13], [28, 39, 48, 33], [4, 20, 21, 5], [9, 8, 16, 17], [32, 36, 44, 40]]
Down = [[20, 19, 18, 17], [43, 42, 41, 44], [15, 14, 13, 16], [47, 46, 45, 48], [23, 22, 21, 24]]
Back = [[13, 18, 10, 5], [41, 37, 29, 33], [1, 17, 22, 6], [25, 40, 45, 34], [2, 9, 21, 14]]

'''
This is in connection with the execute function below
'''
def apply(move, cube):
    for cycle in move:
        temp = cube[cycle[0]]
        for i in range(1, len(cycle)+1):
            temp2 = cube[cycle[i%len(cycle)]]
            cube[cycle[i%len(cycle)]] = temp
            temp = temp2

'''
This function performs the moves on the cube
'''
def execute(moves, cube):
    string = "FBRLUDfbrlud"
    change = ''
    arr = [Front, Back, Right, Left, Up, Down]
    for i in range(len(moves)):
        if moves[i] in string:
            ind = string.index(moves[i])
            change += string[ind]
            if ind > 5:
                ind -= 6
                apply(arr[ind], cube)
                apply(arr[ind], cube)
            apply(arr[ind], cube)
    return change


'''
The align functions contain the moves to complete the top surface of the cube
'''
def align25(cube):
    i=cube.index(25)
    move=['25','u26','uu27','U28','BLU29','RB30','uRB31','lb32', 'LU33', 'B34', 'Ru35', 'LLb36', 'ru37', 'fUU38', 'lU39', 'b40', 'Bru41', 'rB42', 'FlU43', 'Lb44', 'BB45', 'RRu46', 'FFUU47', 'LLU48'][i-25]
    return execute(move, cube)
def align26(cube):
    i=cube.index(26)
    move = ["26", "Bub27", "BUUb28", "29", "rUfu30", "FR31", "LLDfR32", "UULUU33", "RdfR34", "R35", "UFu36", "r37", "rdfR38", "FFR39", "ubU40", "DDfR41", "dfR42", "fR43", "DfR44", "dRR45", "RR46", "DRR47", "DDRR48"][i-26]
    return execute(move, cube)
def align27(cube):
    i = cube.index(27)
    move = ['27', 'LUlu28','29' ,'30' ,'fUlu31' ,'LF32', 'ULu33', 'UUBUU34','uRU35', 'F36','urU37','f38','Ulu39','UUbUU40','DDFUlu41','dFUlu42','FUlu43','DFUlu44','DDFF45','dFF46','FF47','DFF48'][i-27]
    return execute(move, cube)
def align28(cube):
    i=cube.index(28)
    move = ["28", "29", "30", "31", "lldbLB32", "L33", "bDLLB34", "rDDLLR35", "fdFLL36", "BBLBB37", "FdfLL38", "l39", "BDbLL40", "bLB41", "DbLB42", 'DDbLB43', 'dbLB44', 'DLL45', 'DDLL46', 'dLL47','LL48'][i-28]
    return execute(move, cube)
def align1(cube):
    i=cube.index(1)
    move = ["1", "bdBlDDL2", "rlDDRL3", "fdFdlDL4", "BDbDDlDL5", "RDrdlDL6", "FDflDL7", "LDDllDL8", "ldLdBDDb9", "bDBlDDLdlDL10", "rdRBdb11", "fdFDDBDDb12", "dlDL13", "lDL14", "lDDL15", "DlDDL16", "DBdb17", "dBDDb18", "BDDb19", "Bdb20", "BdblDDL21", "bDBBdb22", "rDRDBdb23", "LdllDL24"][i-1]
    return execute(move, cube)
def align2(cube):
    i=cube.index(2)
    move = ["2", "rdRbDDB3", "LdlbddB", "5", "bDBdbDB6", "FDfdbDB7", "LDlbDB8", "9", "bdBdRDDr10", "FDfdbDDBdbDB11", "fdFRdr12", "DbDDB13", "dbDB14", "bDB15", "bDDB16", "Rdr17", "DRdr18", "dRDDr19", "RDDr20", "dRdrbDDB21", "RdrbDDB22", "DRdrbDDB23", "DDRdrbDDB24"][i-2]
    return execute(move, cube)
def align3(cube):
    i=cube.index(3)
    move = ["3", "fDDFddrDR4", "5", "6", "rDRdrDR7","fDFrDR8", "9", "10", "rdRDrdR11", "fDFDrddRDrdR12", "rDDR13", "ddrDR14", "drDR15", "rDR16", "DDrdR17", "drdR18", "rdR19", "DrdR20", "DDrddRDrdR21", "drddRDrdR22", "rddRDrdR23", "DrddRDrdR24"][i-3]
    return execute(move, cube)
def align4(cube):
    i=cube.index(4)
    move = ['4',"5", "6", "7","fDFdfDF8", "9", "10", "11","LdlDLdl12",'fDF13','fddF14','dLDl15','LDl16','dLddl17','Lddl18','Ldl19','DLdl20','fddFdfDF21','fdFdfDF22','dfDFLddl23','fDFLddl24'][i-4]
    return execute(move, cube)

'''
Solvetop calls up the align functions to solve the top surface of the cube
'''
def solvetop(cube):
    solutionls = (align25(cube), align26(cube), align27(cube), align28(cube), align1(cube), align2(cube), align3(cube), align4(cube))
    solution = ''.join(x for x in solutionls)
    return solution

'''
Creates a random cube to solve
'''
def scramble(cube, n = 50):
    string = "FBRLUDfbrlud"
    v = 0
    moves = ''
    for i in range(n):
        v = random.randint(0, 11)
        execute(string[v], cube)
        moves += string[v]
    return moves


'''
Translates the desired moves based on the surface we wish to turn
'''
def toprotate(moves):
    translation = str.maketrans("FBRLUDfbrlud", "LRFBUDlrfbud")
    string = moves.translate(translation)
    return string


'''
Finishes the cube through the first two rows
'''
def edgesfrombottom(cube):
    newresult = ''
    table = ['', 'D', 'DD', 'd']
    place = 0
    nextmove = 0
    for i in range(41, 45):
        if cube[i] < 41 and cube[i] > 32:
            place = cube[i]
            nextmove = (i - place) % 4
            newresult += execute(table[nextmove], cube)
            if place < 37:
                sidemove = 'drDRDFdf'
                for i in range((place+1)%4):
                    sidemove = toprotate(sidemove)
                newresult += execute(sidemove, cube)
            else:
                sidemove = 'DLdldfDF'
                for i in range((place+1)%4):
                    sidemove = toprotate(sidemove)
                newresult += execute(sidemove, cube)
    if len(newresult) > 0:
        return newresult + edgesfrombottom(cube)
    return newresult


'''
Verify cube is finished through the first to rows
'''
def edgesfromsides(cube):
    result = ''
    for i in range(33, 37):
        sidemove = 'drDRDFdf'
        if cube[i] != i:
            for j in range((i-31)%4):
                sidemove = toprotate(sidemove)
            result += execute(sidemove, cube)
            result += edgesfrombottom(cube)
    return result


'''
Create a cross on the bottom face
'''
def flipbottomedges(cube):
    result = ''
    num = 0
    for i in range(45, 49):
        if cube[i] > 44:
            num += 1
    if num == 0:
        result += execute('FLDldfBRDrdRDrdb' , cube)
    if num == 2:
        while cube[48] < 45 or cube[47] > 44:
            result += execute('D', cube)
        if cube[46] > 44:
            result += execute('FLDldf', cube)
        else:
            result += execute('RDFdfr', cube)
    return result


'''
Put the cross in the correct position
'''
def positionbottomedges(cube):
    result = ''
    correct = 0
    while correct < 2:
        correct = 0
        for i in range(45, 49):
            if cube[i] == i:
                correct += 1
        if correct < 2:
            result += execute('D', cube)
    if correct == 2:
        move = 'FDfDFDDfRDrDRDDrD'
        adjmove ='LDlDLDDlD'
        if cube[46] == 46 and cube[48] == 48:
            result += execute(move, cube)
        elif cube[45] == 45 and cube[47] == 47:
            move = toprotate(move)
            result += execute(move, cube)
        elif cube[45] == 45 and cube[48] == 48:
            result += execute(adjmove, cube)
        elif cube[45] == 45 and cube[46] == 46:
            adjmove = toprotate(adjmove)
            result += execute(adjmove, cube)
        elif cube[46] == 46 and cube[47] == 47:
            for i in range(2):
                adjmove = toprotate(adjmove)
            result += execute(adjmove, cube)
        elif cube[47] == 47 and cube[48] == 48:
            for i in range(3):
                adjmove = toprotate(adjmove)
            result += execute(adjmove, cube)
    return result


'''
Puts bottom corners in the correct position
'''
def positionbottomcorners(cube):
    result = ''
    num = 0
    move = 'rDLdRDld'
    for i in range(21, 25):
        if (cube[i] - i)%4 == 0:
            num += 1
    if num == 0:
        result += execute(move, cube)
    if num != 4:
        if (cube[24] - 24)%4 == 0:
            while (cube[23] - 23)%4 != 0:
                result += execute(move, cube)
        elif (cube[21] - 21)%4 == 0:
            move = toprotate(move)
            while (cube[23] - 23)%4 != 0:
                result += execute(move, cube)
        elif (cube[22] - 22)%4 == 0:
            for i in range(2):
                move = toprotate(move)
            while (cube[23] - 23)%4 != 0:
                result += execute(move, cube)
        elif (cube[23] - 23)%4 == 0:
            for i in range(3):
                move = toprotate(move)
            while (cube[21] - 21)%4 != 0:
                result += execute(move, cube)
    return result


'''
Corrects the orientation of the corners
'''
def rotatebottomcorners(cube):
    result = ''
    for i in range(4):
        while cube[21] < 21:
            result += execute('buBUbuBU', cube)
        result += execute('D', cube)
    return result


'''
Solvecube calls on all functions to solve a rubik's cube
'''
def solvecube(cube):
    result = ""
    result += solvetop(cube)
    result += edgesfrombottom(cube)
    result += edgesfromsides(cube)
    result += flipbottomedges(cube)
    result += positionbottomedges(cube)
    result += positionbottomcorners(cube)
    result += rotatebottomcorners(cube)
    return result

'''
test allows us to run multiple random cubes through the program and verifies
that each cube is solved correctly
'''
def test(n):
    flag=True
    for i in range(n): #Tests the function on n cubes
        cube=list(range(49)) #Initializes a solved cube
        t=scramble(cube) #Randomizes the cube
        t+=solvecube(cube) #Solves the cube
        if cube!=list(range(49)): #Checks that the cube is solved
            flag=False
        testcube=list(range(49));
        u=execute(t,testcube) #Checks that the moves actually
        if testcube!=list(range(49)): # solve the cube.
            flag=False
    if flag:
        print("The code seems to be working")
if __name__=="__main__":
    cube = []
    A = time.time()
    for i in range(49):
        cube.append(i)
    newcube = scramble(cube)
    print(test(1000))
    B = time.time()
    print(newcube)
    print(solvecube(cube))
    print(abs(A-B))
