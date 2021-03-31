class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    
    def peek(self):
        return self.first
    
    def enqueue(self, value):
        theNode = Node(value)
        if(self.length == 0):
            self.first = theNode
            self.last = theNode
        else:
            self.last.next = theNode 
            self.last = theNode 
        self.length += 1
    
    def dequeue(self):
        #check
        if(self.length <= 0):
            return "error. there is no item"
        returnVal = self.first
        if(self.length == 1):
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1 
        return returnVal

    def isEmpty(self):
        if(self.length <= 0):
            return True
        else: 
            return False
        

myQueue = Queue()

myQueue.enqueue("Joy")
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

myQueue.enqueue("Matt")
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

myQueue.enqueue("Pavel")
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

myQueue.enqueue("Samir")
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])



print("isEmpty:",myQueue.isEmpty())

print(myQueue.dequeue().value)
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

print(myQueue.dequeue().value)
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

print(myQueue.dequeue().value)
print("peek",myQueue.peek().value)
print(["first:", myQueue.first.value, "last:", myQueue.last.value, "length:", myQueue.length])

print(myQueue.dequeue().value)
print("peek",myQueue.peek())
print(["first:", myQueue.first, "last:", myQueue.last, "length:", myQueue.length])

print(myQueue.dequeue())

# //Joy
# //Matt
# //Pavel
# //Samir