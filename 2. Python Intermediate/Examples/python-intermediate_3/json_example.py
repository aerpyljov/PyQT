import json
import  vector
p = 'c:/tmp/file.json'
x = vector.vector(1,2,3)
data = [1,2,3,x]
class mySerialize(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, vector.vector):
            d = o.__dict__
            d.update({'classType': o.__class__.__name__})
            return d
        return super(mySerialize, self).default(o)


json.dump(data, open(p, 'w'), indent=4, cls=mySerialize)
y = json.load(open(p))


