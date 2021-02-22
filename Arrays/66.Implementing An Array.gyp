class MyArray:
    def __init__(self):
        self.length=0
        self.data={}
    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length]=item
        self.length += 1
    
    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem
    
    def delete(self, index):
        theItem = self.data[index]
        for i in range(index,self.length-1):
            print(i)
            self.data[i] = self.data[i+1] 
        del self.data[self.length-1]
        self.length -= 1
        return theItem
    
    

arr1 = MyArray()
arr1.push('a')
arr1.push('b')
arr1.push('c')
arr1.push('d')
print(arr1.get(0) ) #a
print(arr1.data)    #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}
arr1.pop()
print(arr1.data)    #{0: 'a', 1: 'b', 2: 'c'}
arr1.delete(1)
print(arr1.data)    #{0: 'a', 1: 'cf'}
