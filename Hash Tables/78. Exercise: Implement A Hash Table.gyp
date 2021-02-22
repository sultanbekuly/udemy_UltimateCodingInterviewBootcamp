class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for i in range(size)]
    
    def __str__(self):
        return str(self.__dict__)
    
    def _hash(self, key):
        return len(key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)        
        self.data[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        if(self.data[index] != []):
            for i in range(len(self.data[index])):
                if(self.data[index][i][0] == key):
                    return self.data[index][i][1]
            return None
        else:
            return None
    
    def keys(self):
        keys = []
        for i in self.data:
            if(i!=[]):
                for j in i:
                    keys.append(j[0])
        return keys

    def values(self):
        values = []
        for i in self.data:
            if(i!=[]):
                for j in i:
                    values.append(j[1])
        return values
    

        
    
    
test = HashTable(16)
print(test._hash('a'))
print(test._hash('b'))
print(test._hash('10'))
print(test._hash('grapes'))

test.set('grapes',10000)
test.set('a',1)
test.set('b',2)
print(test)

print("grapes",test.get('grapes'))
print('a',test.get('a'))
print('b',test.get('b'))


print('keys',test.keys())

print('values',test.values())


