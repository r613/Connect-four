from User import Input
from User import Print
import os 
from Modify import sstm
def Round(matrix,size_v,size_h,team,round):
    sstm()
    Print(matrix)
    print "You are at round No: {}".format(round)
    print "Team {} now it's your turn".format(team)
    
    matrix = placing(matrix,size_v,size_h,team)#Places the piece in the matrix ()
    
    
    
    return matrix

def placing(matrix,size_v,size_h,char):
    row = Input("In what column would you like to place your piece?")
    if row < size_h:
        pass
    else:
        return placing(matrix,size_v,size_h,char)
    for i in range(0,size_v-1): #we don't count the last row - since we try checking what's under every row (and if we check what's under the last row, we can get lots of errors)
        if matrix[i+1][row-1] != " ": # If the row is not empty -1 for the row since the row starts from 0
            matrix[i][row-1] = char
            return matrix
            #do what happens in a move
        else:
            pass
    matrix[size_v-1][row-1] = char
    return matrix
