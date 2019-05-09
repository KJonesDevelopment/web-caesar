import math
def rotate_string(mess, value):
    mess = mess
    alphaLOW = "abcdefghijklmnopqrstuvwxyz"
    alphaCAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    test = ""
    for i in mess:
        if not i.isalpha():
            test = test + i
            continue
        if i.islower():
            alphabet = alphaLOW
        else: 
            alphabet = alphaCAP
        place = alphabet.find(i)
        newPlace = place + value
        if newPlace > 25:
            newPlace = newPlace % 26
        char = alphabet[newPlace]
        test = test + char
    return test