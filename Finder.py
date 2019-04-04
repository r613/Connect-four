
def finder(matrix,size_v,size_h): #Checks (using other functions) if there are any 4-in-a-rows
    for row in range(size_v):
        for column in range(size_h):
            if matrix[row][column] != " ":
                
                if down(matrix,row,column,matrix[row][column],size_v) > 3: return matrix[row][column] #Recursive - if there are > 3 pieces (from this space and downwards) - There is a winner 
                elif right(matrix,row,column,matrix[row][column],size_h) > 3: return matrix[row][column]
                elif diag(matrix,row,column,matrix[row][column],size_v,size_h) > 3: return matrix[row][column]
                elif daig(matrix,row,column,matrix[row][column],size_v,size_h) > 3: return matrix[row][column]
                    #the code returns the value of the piece we are holding at - The winning team X or O 
            else:
                pass 
    #if we get here - we got no 4-in-a-rows and don't return anything - which is False
def down(matrix,row,column,char,size_v): #Recursive 
    if matrix[row][column] == char and row+1 < size_v: #if this piece equals to the piece before it (char)
        return down(matrix,row+1,column,char,size_v) + 1 #return 1 + how many more char 's there are in this direction (1+ for this piece)
    elif matrix[row][column] == char:
        return 1
    else:
        return 0
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
        return 0
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

def full(matrix,size_v,size_h):
    for row in matrix:
        for space in row:
            if space == " ":
                return False
    return True
