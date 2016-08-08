<<<<<<< HEAD
#python implementation of conways game of life

# om död och precis 3 grannar => levande
#om levande och färre än två eller fler än 3 granar => dör

#TODO: gör test för se om ett givet seed överlever mer än x generationer, UTAN direkt upprepning (iaf inte exakt samma)
#Om det testet passar, spara seedet i txt dokument med namn unikt för seedet (dagens datum? baserat på innehållet på nåt smart sätt? random tal?)
#gör nån enkel generator av seeds så kan testa igenom många
#sen köra igenom vissa för att se vilka som är verkligt intressanta

import copy
import time
#returns number of alive neighbours of given cell
def neig(r,c):
    global dim
    n=0
    if c>0:
        if r>0:
            n+= board[r-1][c-1]
        n+= board[r][c-1]
        if r < (dim-1):
            n+= board[r+1][c-1]
    if c < (dim-1):
        if r>0:
            n+= board[r-1][c+1]
        n+= board[r][c+1]
        if r<(dim-1):
            n+= board[r+1][c+1]
    if r<(dim-1):
        n+= board[r+1][c]
    if r>0:
        n+= board[r-1][c]
    return n

	#returns string of the current board (with * for alive and . for dead)
def printBoard():
    global dim
    theString=""
    for x in range(dim):
        for y in range(dim):
            if board[x][y]:
                theString+="* "
            else:
                theString+=". "
        theString+="\n"

    return theString

#run the simulation, can be either with "press enter to continue" or a given amount of times
def runLife(pr,nr):
	
    global board
    korv=0
    while korv <=nr:
        if(pr):
            print(printBoard())
        newBoard=copy.deepcopy(board)
        for x in range(dim):
            for y in range(dim):
                ne = neig(y,x)
                if ne < 2 or ne >3:
                    newBoard[y][x]=0
                elif ne ==3:
                    #print(str(x)+" "+str(y))
                    newBoard[y][x]=1
        if board == newBoard:
            print("STILLASTÅENDE")
            return
        board=copy.deepcopy(newBoard)
        time.sleep(0.2)
        #in=input("Press Enter to continue, enter 'q' to quit...")
        korv+=1

        
def getFromFile():
    file = open('seeds/seed.cw', 'r')
    global dim
    dim= len(file.readline())-1
    board = [[0 for x in range(dim)] for y in range(dim)]
    file.seek(0)

    line_nr=0
    line_pos=0

    for line in file:
        for ch in line:
            if ch != "\n":
                board[line_nr][line_pos]=int(ch)
                line_pos+=1
        line_pos=0
        line_nr+=1
    return board



def saveToFile(bo,filename):
    global dim
    with open(filename, "a") as myfile:
        for x in range(dim):
            for y in range(dim):
                myfile.write(str(bo[x][y]))
            myfile.write("\n")
            






board = getFromFile()
runLife(1,100)
saveToFile(board,"seeds/end.cw")
=======
#python implementation of conways game of life

# om död och precis 3 grannar => levande
#om levande och färre än två eller fler än 3 granar => dör

#TODO: gör test för se om ett givet seed överlever mer än x generationer, UTAN direkt upprepning (iaf inte exakt samma)
#Om det testet passar, spara seedet i txt dokument med namn unikt för seedet (dagens datum? baserat på innehållet på nåt smart sätt? random tal?)
#gör nån enkel generator av seeds så kan testa igenom många
#sen köra igenom vissa för att se vilka som är verkligt intressanta

import copy
import time
#returns number of alive neighbours of given cell
def neig(r,c):
    global dim
    n=0
    if c>0:
        if r>0:
            n+= board[r-1][c-1]
        n+= board[r][c-1]
        if r < (dim-1):
            n+= board[r+1][c-1]
    if c < (dim-1):
        if r>0:
            n+= board[r-1][c+1]
        n+= board[r][c+1]
        if r<(dim-1):
            n+= board[r+1][c+1]
    if r<(dim-1):
        n+= board[r+1][c]
    if r>0:
        n+= board[r-1][c]
    return n

	#returns string of the current board (with * for alive and . for dead)
def printBoard():
    global dim
    theString=""
    for x in range(dim):
        for y in range(dim):
            if board[x][y]:
                theString+="* "
            else:
                theString+=". "
        theString+="\n"

    return theString

#run the simulation, can be either with "press enter to continue" or a given amount of times
def runLife(pr,nr):
	
    global board
    korv=0
    while korv <=nr:
        if(pr):
            print(printBoard())
        newBoard=copy.deepcopy(board)
        for x in range(dim):
            for y in range(dim):
                ne = neig(y,x)
                if ne < 2 or ne >3:
                    newBoard[y][x]=0
                elif ne ==3:
                    #print(str(x)+" "+str(y))
                    newBoard[y][x]=1
        if board == newBoard:
            print("STILLASTÅENDE")
            return
        board=copy.deepcopy(newBoard)
        time.sleep(0.2)
        #in=input("Press Enter to continue, enter 'q' to quit...")
        korv+=1

        
def getFromFile():
    file = open('seed.cw', 'r')
    global dim
    dim= len(file.readline())-1
    board = [[0 for x in range(dim)] for y in range(dim)]
    file.seek(0)

    line_nr=0
    line_pos=0

    for line in file:
        for ch in line:
            if ch != "\n":
                board[line_nr][line_pos]=int(ch)
                line_pos+=1
        line_pos=0
        line_nr+=1
    return board



def saveToFile(bo,filename):
    global dim
    with open(filename, "a") as myfile:
        for x in range(dim):
            for y in range(dim):
                myfile.write(str(bo[x][y]))
            myfile.write("\n")
            






board = getFromFile()
runLife(1,100)
saveToFile(board,"end.cw")
>>>>>>> b71ba607d2b5ecbf15fba9356dfbcdc15ae4f306
