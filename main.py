import os
#Connect four 
from Gaming import Round
from Gaming import placing

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
        matrix = Round(matrix,size_v,size_h,"O",round)
        if round > 15:
            game_on = False


        

menu()