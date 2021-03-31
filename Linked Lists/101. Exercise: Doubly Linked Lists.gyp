class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedLists:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        this_Node = Node(value)
        this_Node.prev = self.tail 
        self.tail.next = this_Node
        self.tail = this_Node
        self.length += 1

    def prepend(self, value):
        this_Node = Node(value)
        self.head.prev = this_Node
        this_Node.next = self.head
        self.head = this_Node
        self.length += 1

    def printList(self):
        arr = []
        currentNode = self.head
        while(currentNode != None):
            arr.append(currentNode.data)
            currentNode = currentNode.next
        return arr
    
    def printListRev(self):
        arr = []
        currentNode = self.tail
        while(currentNode != None):
            arr.append(currentNode.data)
            currentNode = currentNode.prev
        return arr

    def insert(self, index, value):
        #check
        if(index==0):
            self.prepend(value)
        if(index>=self.length):
            self.append(value)

        this_Node = Node(value)
        currentNode = self.head
        i = 0
        while(True):
            if(i==index-1):
                currentNode.next,this_Node.next   = this_Node, currentNode.next
                currentNode.next.next.prev = currentNode.next
                currentNode.next.prev = currentNode
                self.length += 1
                return True
            currentNode = currentNode.next
            i+=1
        return False

    def remove(self, index):
        #check
        if(type(index)!=int or index>=self.length):
            return "error input"
        
        currentNode = self.head
        if(index == 0):#index==0
            self.head = self.head.next
            self.head.prev = None
        elif(index == self.length-1):#index==-1
            for _ in range(0,index-1):
                currentNode = currentNode.next
            currentNode.next = None
            self.tail = currentNode
        else:
            for _ in range(0,index-1):
                currentNode = currentNode.next
            currentNode.next.next.prev = currentNode
            currentNode.next = currentNode.next.next

        self.length -= 1

myLinkedLists = DoublyLinkedLists(10)

myLinkedLists.append(5)
myLinkedLists.append(16)

myLinkedLists.prepend(1)

print("N",myLinkedLists.printList())
print("R",myLinkedLists.printListRev())

print("myLinkedLists.insert(1,7)")
myLinkedLists.insert(1,7)

print("N",myLinkedLists.printList())
print("R",myLinkedLists.printListRev())

print("myLinkedLists.insert(3,3)")
myLinkedLists.insert(3,3)



print("N",myLinkedLists.printList())
print("R",myLinkedLists.printListRev())

print("#Removing")
myLinkedLists.remove(5)
myLinkedLists.remove(3)
myLinkedLists.remove(0)

print("N",myLinkedLists.printList())
print("R",myLinkedLists.printListRev())
print(myLinkedLists.head.data)
print(myLinkedLists.tail.data)

