import pickle
p = 'c:/tmp/file.txt'
x = [1,2,3, {1:3}]
pickle.dump(x, open(p, 'w'))

y = pickle.load(open(p))