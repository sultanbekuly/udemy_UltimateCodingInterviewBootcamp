class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        return self.__dict__

    def peek(self):
        if( self.list == []):
            return None
        else:
            return self.list[ len(self.list) - 1]
    
    def push(self, value):
        self.list.append(value)
        
    def pop(self):
        self.list.pop()
        
myStack = Stack()

myStack.push("Google")
print(myStack.peek())

myStack.push("Udemy")
print(myStack.peek())

myStack.push("Discord")
print(myStack.peek())

print("#pop")
myStack.pop()
print(myStack.peek())

myStack.pop()
print(myStack.peek())

myStack.pop()
print(myStack.peek())


