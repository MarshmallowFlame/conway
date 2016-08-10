#python implementation of conways game of life


import time
import math
#returns number of alive neighbours of given cell
def neig(r,c,board,dim):
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
def printBoard(board,dim):
    theString=""
    for x in range(dim):
        for y in range(dim):
            if board[x][y]:
                theString+="* "
            else:
                theString+=". "
        theString+="\n"

    return theString

#changes the board to one step ahead in time, while also passing along if the board is the same as previous
def iterate(board,dim):
    newBoard=[[0 for x in range(dim)] for y in range(dim)]
    for x in range(dim):
        for y in range(dim):
            ne = neig(y,x,board,dim)
            
            if ne ==3 or (ne == 2 and board[y][x]):
                #print(str(x)+" "+str(y))
                newBoard[y][x]=1

        if board == newBoard:
            return newBoard,0
            

    return newBoard,1




#runs the simulation the stated number of times
def runLife(pr,nr,board,dim):
    korv=0
    while korv <=nr:
        if(pr):
            print(printBoard(board,dim))
            
        board,err =iterate(board,dim)
        if not err:
            if pr:
                print("SAMMA")
            return 0
        
       

        if pr:
            time.sleep(0.2)
        #in=input("Press Enter to continue, enter 'q' to quit...")
        korv+=1
    return 1

#returns a board from file named "seed.cw" in seeds     
def getFromFile(dim):
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


#Saves the passed board to a file
def saveToFile(bo,filename,dim):
    with open(filename, "a") as myfile:
        for x in range(dim):
            for y in range(dim):
                myfile.write(str(bo[x][y]))
            myfile.write("\n")
            
#returns a board from a given seed being a integer.
#Works by converting the integer to binary and letting each 1 or 0 be a cell
#(adding zeros to beginning to fill up the board)
def getFromSeed(seed, dim):
    
    seed="{0:b}".format(seed)
    
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

#runs a loop to find the seeds that does not die after some generations, returns the list of successful seeds
def findUsefulSeeds(dim):
    succ=[]
    
    start = 0
    end = 2**((dim)**2)
    print(end)


    percents = end//100
    
    for i in range(end):
        if i%percents ==0:
            print (str(i//percents)+"% done")

        
        board = getFromSeed(i,dim)
        if runLife(0,5,board,dim):
            succ.append(i)
    print(len(succ))
    return succ    

seedToUse = findUsefulSeeds(4)[500]

runLife(1,5,getFromSeed(seedToUse,5),5)

