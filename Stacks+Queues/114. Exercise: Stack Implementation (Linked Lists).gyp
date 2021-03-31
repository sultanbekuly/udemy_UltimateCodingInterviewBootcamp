class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None     #tail
        self.bottom = None  #head
        self.length = 0
    
    def peek(self):
        return self.top
    
    def push(self, value):
        theNode = Node(value)
        if(self.length == 0):
            self.top = theNode
            self.bottom = theNode
        else:
            theNode.next = self.top
            self.top = theNode
        self.length += 1

    def pop(self):
        #check 
        if(self.isEmpty()):
            return "error. the stack is empty"
        returnVal = self.top
        if(self.length == 1):
            self.top = None
            self.bottom = None
        else:
            self.top =  self.top.next
        self.length -= 1
        return returnVal

    def isEmpty(self):
        if(self.length <= 0):
            return True
        else:
            return False

    def printList(self):
        arr = []
        theNode = self.top
        while (theNode != None):
            arr.append(theNode.value)
            theNode = theNode.next
        return arr

myStack = Stack()

myStack.push("Google")
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top.value,"bottom:",myStack.bottom.value)

myStack.push("Udemy")
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top.value,"bottom:",myStack.bottom.value)

myStack.push("Discord")
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top.value,"bottom:",myStack.bottom.value)

print("#pop")
myStack.pop()
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top.value,"bottom:",myStack.bottom.value)

myStack.pop()
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top.value,"bottom:",myStack.bottom.value)

myStack.pop()
print(myStack.peek())
print(myStack.printList(),"top:",myStack.top,"bottom:",myStack.bottom)


