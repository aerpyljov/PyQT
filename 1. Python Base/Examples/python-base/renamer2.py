import os

root = os.path.dirname(__file__)
files = os.listdir(root)
arg = []
for f in files:
	if os.path.isfile(os.path.join(root, f)):
		if os.path.splitext(f)[-1] == '.txt':
			arg.append(os.path.join(root, f))

newName = raw_input('Enter name: ')
if newName:
    for i, f in enumerate(arg):
        d = os.path.dirname(f)
        name, ext = os.path.splitext( os.path.basename(f) )
        fName = newName + '_' + str(i+1).zfill(3) + ext
        fullPath = os.path.join(d, fName)
        os.rename(f, fullPath)

raw_input()