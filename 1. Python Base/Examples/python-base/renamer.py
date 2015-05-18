import sys
import os

arg = sys.argv[1:]

newName = raw_input('Enter name: ')
if newName:
    for i, f in enumerate(arg):
        d = os.path.dirname(f)
        name, ext = os.path.splitext( os.path.basename(f) )
        fName = newName + '_' + str(i+1).zfill(3) + ext
        fullPath = os.path.join(d, fName)
        os.rename(f, fullPath)

raw_input()