#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script can help you, if you have a lot of photos, and every name has digits in the end.
The script allows you to achieve the following goals:
- Put photos from different cameras into differenf folders.
- Rename the photos: change the word and the sequence number (start from 1, add padding).


Requirements:
- MS Windows.
- Python 2.7.
- A folder with photos.



"""


import os
import sys
import shutil


# Define defaul settings
padding = 4


# Define functions
def getListOfFiles(folder):
"Return a list of files in a folder (not subfolders)"
    tmp = os.listdir(folder)
    files = []
    for t in tmp:
        if os.path.isfile( os.path.join(folder, t) ):
            files.append(t)
    return files

    
def getSequences(files):
"Return a set of sequences (a list of unique first parts of file names, before frame number)"
    sequences = set()
    for f in files:
        name, ext = os.path.splitext(f)
        while name[-1].isdigit():
            name = name[:-1]
        sequences.append(name)
    return sequences
    

def getNewSequenceNames(sequences):
"Ask the user to enter new names for each sequence and return them as values of a dictionary (old names are keys)"
    newSequenceNames = dict.fromkeys(sequences)
    for s in sequences:
        usedSequenceNames = ", ".join(newSequenceNames.values())
        message = """Enter a new name for a sequence with name "{0}".\nYou have already used these names: {1}.\nType new name: """.format(s, usedSequenceNames)
        newSequenceName = raw_input(message).decode('cp866')
        newSequenceNames[s] = newSequenceName
    return newSequenceNames


def makeFoldersForSequences(path, newSequenceNames):
    for s in newSequenceNames:
        newSequenceName = newSequenceNames[s]
        outFolder = os.path.join(path, newSequenceName)
        if not os.path.exists(outFolder):
            os.mkdir(outFolder)


def ListOfFilesForSequence(files, sequence):
"Return a list of files with the sequence name"
    sequenceFiles = []
    for f in files:
        if f.startswith(sequence):
        sequenceFiles.append(f)
    return sequenceFiles     
            
            
def getFrames(sequenceFiles):
"Return a list of frames based on a list of files"
    frames = []
    for f in sequenceFiles:
        name, ext = os.path.splitext(f)
        fullName = name
        while name[-1].isdigit():
            name = name[:-1]
        digits = int(fullName.replace(name, ''))
        frames.append(digits)
    return frames        

    
def getOffset(frames):
"Return an offset as a digit based on a list of frames"
    offset = min(frames) - 1
    return offset
       
        
                                                    def copySequence(path, files, newSequenceNames):
                                                        for i, f in enumerate(files):
                                                            old = os.path.join(path, f)
                                                            name, ext = os.path.splitext(f)
                                                            newName = newSequenceName + '_' + str(frames[i]-offset).zfill(padding) + ext
                                                            new = os.path.join(path, newSequenceName, newName)
                                                            if os.path.exists(new):
                                                                os.remove(new)
                                                            shutil.copy2(old, new)    



    
# Find the name of the folder with photos for renaming
scriptPath = sys.argv[0]
path = os.path.dirname(scriptPath)

 
# Find sequences, ask the user to enter new names for sequences and make a folder for each sequence with new name
files = getListOfFiles(path)

sequences = getSequences(files)

newSequenceNames = getNewSequenceNames(sequences)

makeFoldersForSequences(path, newSequenceNames)









    
# search missing frames
fullrange = range(min(frames), max(frames)+1)
miss = []
for i in fullrange:
    if not i in frames:
        miss.append(i)
# message
print 'Miss frames:', miss

a = raw_input('Remove old files? [y/n]: ')
if a == 'y' or a == 'Y':
    for f in files:
        os.remove(os.path.join(path, f))
print 'Complete!!!'
raw_input()


