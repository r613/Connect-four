import os
def Input(text):
    try:
        return input(text)
    except:
        print "Nice Try! Numbers Only."
        return Input(text)
def Print(matrix):
    text = ""
    for row in matrix:
        text += "\n" + str(Print_row(row))
    text += "\n"
    for i in range(len(row)):
        text += " | "
    text += "\n"
    for i in range(len(row)):
        text  += (" "*(2-len(str(i)))) + "{} ".format(i+1)
            
    print text
def Print_row(row):
    text = ""
    for i in row:
        text += "|_{}".format(i)
    return text