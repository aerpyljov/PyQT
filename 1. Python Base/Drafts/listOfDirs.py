# -*- coding: utf-8 -*-

file = open('Dirs.txt').readlines()

""""
for line in enumerate(file):
    print line
"""
    



def stringsToListOfLists(file):
    ListOfLists = []
    for position, string in enumerate(file):
        stringOfFileAsTuple = []
        stringOfFileAsTuple.append(position)
        stringOfFileAsTuple.append(0)
        for char in string:
            if char == '\t':
                stringOfFileAsTuple[1] += 1
            else:
                break
        newString = string.strip()
        stringOfFileAsTuple.append(newString)
        ListOfLists.append(stringOfFileAsTuple)
    return ListOfLists








def makeListOfDirs(file):
    folders = []
    ListOfLists = stringsToListOfLists(file)
    levels = [level for position, level, string in ListOfLists]
    levels = list(set(levels))
    minLevel = min(levels)
    currentPosition = -1
    for position, level, string in ListOfLists:
        if level == minLevel:
            folders.append(string)
    return folders
        
        
        
a = makeListOfDirs(file)
print a