#python implementation of conways game of life


import time
import math
#returns number of alive neighbours of given cell
def neig(r,c,board):
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
def printBoard(board):
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
def iterate(board):
    global dim
    newBoard=[[0 for x in range(dim)] for y in range(dim)]
    for x in range(dim):
        for y in range(dim):
            ne = neig(y,x,board)
            if ne < 2 or ne >3:
                newBoard[y][x]=0
            elif ne ==3:
                #print(str(x)+" "+str(y))
                newBoard[y][x]=1

        if board == newBoard:
            return newBoard,0
            

    return newBoard,1




    
def runLife(pr,nr,board):
    korv=0
    while korv <=nr:
        if(pr):
            print(printBoard(board))
            
        board,err =iterate(board)
        if not err:
            if pr:
                print("SAMMA")
            return 0
        
       

        if pr:
            time.sleep(0.2)
        #in=input("Press Enter to continue, enter 'q' to quit...")
        korv+=1
    return 1
        
def getFromFile():
    global dim
    with open('seeds/seed.cw', 'r') as file:
        
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
            

def getFromSeed(seed, sideLength):
    global dim
    
    seed="{0:b}".format(seed)

    dim=sideLength

    
    if not len(seed)==dim**2:
        for i in range(dim**2 - len(seed)):
            seed="0"+seed


    board = [[0 for x in range(dim)] for y in range(dim)]

    x=0
    y=0
    for ch in seed:
        if x==dim:
            x=0
            y+=1
        board[x][y]=int(ch)
        x+=1
    
    return board

         
def findUsefulSeeds(sideLength):
    succ=[]
    global dim
    dim = sideLength
    
    start = 0
    end = 2**((dim)**2)
    print(end)


    percents = end//100
    
    for i in range(end):
        if i%percents ==0:
            print (str(i//percents)+"% done")

        
        board = getFromSeed(i,dim)
        if runLife(0,5,board):
            succ.append(i)
    print(len(succ))
    return succ    

seedToUse = findUsefulSeeds(4)[500]

runLife(1,5,getFromSeed(seedToUse,4))

