import os
path = 'c:/tmp'
fileName = 'settings.txt'

class settingsClass(object):
    def __init__(self):
        self.fullPath = os.path.join(path, fileName)
        if not os.path.exists(self.fullPath):
            open(self.fullPath, 'w').close()

    def __readFile(self):
        f = open(self.fullPath)
        text = f.readlines()
        f.close()
        data = {}
        for line in text:
            key, value = line.strip().split('=')
            data[key] = value
        return data

    def __writeFile(self, data):
        f = open(self.fullPath, 'w')
        for k, v in data.items():
            f.write('%s=%s\n' % (k, v))
        f.close()

    def readSettings(self):
        data = self.__readFile()
        return data

    def writeSettings(self, data):
        # check
        self.__writeFile(data)

    def readValue(self, key):
        data = self.__readFile()
        return data.get(key)

    def writeValue(self, key, value):
        data = self.__readFile()
        data[key] = value
        self.__writeFile(data)

s = settingsClass()
s.writeValue('key1', 1000)
s.writeValue('key2', 100)
s.readValue('key1')
s.readValue('name')
s.readSettings()
d = {1:2, 3:4}
s.writeSettings(d)
