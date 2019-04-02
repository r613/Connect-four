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
    print text
def Print_row(row):
    text = ""
    for i in row:
        text += "|_{}".format(i)
    return text