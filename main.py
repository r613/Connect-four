#Connect-Four v2.1
from Finder import finder
from Finder import daig
from Finder import diag
from Finder import right
from Finder import down
from Finder import full
import os
from Gaming import Round
from Gaming import placing
from User import Print
from Modify import size
def menu():
    matrix = []
    size_v,size_h = size()
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
            Print(matrix)
            print "Team {} Won!".format(finder(matrix,size_v,size_h))
            break
        matrix = Round(matrix,size_v,size_h,"O",round)
        
        if finder(matrix,size_v,size_h):
            Print(matrix)
            print "Team {} Won!".format(finder(matrix,size_v,size_h))
            break

        if full(matrix,size_v,size_h):
            Print(matrix)
            print "Tie! The board is full!"
            game_on = False 

menu()