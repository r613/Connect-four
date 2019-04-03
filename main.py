import os
#Connect four 
from Gaming import Round
from Gaming import placing
from User import Print

def menu():
    matrix = []
    size_v = 6
    size_h = 7

    for i in range(size_v): #This creates the matrix
        row = []
        for a in range(size_h):
            row.append(' ')
        matrix.append(row)


    game_on = True
    round = 0

    while game_on:
        
        round += 1
        matrix = Round(matrix,size_v,size_h,"X",round)
        
        if finder(matrix,size_v,size_h):
            print "Somebody won!"
            Print(matrix)
            game_on = False
        
        matrix = Round(matrix,size_v,size_h,"O",round)
        

        if finder(matrix,size_v,size_h):
            print "Somebody won!"
            Print(matrix)
            game_on = False
        
        
        if round > 15:
            game_on = False
def finder(matrix,size_v,size_h):
    for row in range(size_v):
        for column in range(size_h):
            if matrix[row][column] != " ":
                print down(matrix,row,column,matrix[row][column],size_v)
                print right(matrix,row,column,matrix[row][column],size_h)
                print diag(matrix,row,column,matrix[row][column],size_v,size_h)
                print daig(matrix,row,column,matrix[row][column],size_v,size_h)
                if down(matrix,row,column,matrix[row][column],size_v) > 3:
                    print "down"
                    return True
                elif right(matrix,row,column,matrix[row][column],size_h) > 3:
                    print "right"
                    return True
                elif diag(matrix,row,column,matrix[row][column],size_v,size_h) > 3:
                    print "Diag"
                    return True
                elif daig(matrix,row,column,matrix[row][column],size_v,size_h) > 3:
                    print "Daig"
                    return True
            else:
                pass
def daig(matrix,row,column,char,size_v,size_h): #row + 1 column - 1 
    #if this space is also the same as the one as 
    if matrix[row][column] == char:
        if row + 1 < size_v and column > 0:
            return daig(matrix,row + 1, column - 1, char, size_v, size_h) + 1
        return 1
    else:
        return 0

def diag(matrix,row,column,char,size_v,size_h): # row +1 column +1
    if matrix[row][column] == char:
        if row + 1 < size_v and column + 1 < size_h:
            return diag(matrix,row + 1, column +1, char, size_v , size_h) +1    
        else:
            return 1
    else:
        pass
def right(matrix,row,column,char,size_h):
    if matrix[row][column] == char and column + 1 < size_h:
        return right(matrix,row,column+1,char,size_h) + 1
    elif matrix[row][column] == char:
        return 1
    else:
        return 0
def down(matrix,row,column,char,size_v):
    if matrix[row][column] == char and row+1 < size_v:
        return down(matrix,row+1,column,char,size_v) + 1
    elif matrix[row][column] == char:
        return 1
    else:
        return 0


        

menu()