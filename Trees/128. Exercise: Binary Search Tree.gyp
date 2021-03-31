class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        theNode = Node(value)
        if(self.root == None):
            self.root = theNode
            return
        else:
            # print("###",theNode.value)
            currentNode = self.root
            while(True):
                # print("##",currentNode.value)
                if(currentNode.value < value):
                    if(currentNode.right == None):
                        # print("#","currentNode.right = theNode")
                        currentNode.right = theNode
                        return
                    else:
                        currentNode = currentNode.right
                elif(currentNode.value > value):
                    if(currentNode.left == None):
                        # print("#","currentNode.left = theNode")
                        currentNode.left = theNode
                        return
                    else:
                        currentNode = currentNode.left
                else:
                    # print("#","error. the value already in the BST")
                    return "error. the value already in the BST"

    def lookup(self, value):
        currentNode = self.root
        while(currentNode != None):
            if (currentNode.value < value):
                currentNode = currentNode.right
            elif(currentNode.value > value):
                currentNode = currentNode.left
            else: #equal
                return currentNode
        return None
    
    def _lookupWithParent(self, value):
        currentNode = self.root
        parentNode = None
        isChildRight = None
        while(currentNode != None):
            if (currentNode.value < value):
                parentNode = currentNode
                currentNode = currentNode.right
                isChildRight = True
            elif(currentNode.value > value):
                parentNode = currentNode
                currentNode = currentNode.left
                isChildRight = False
            else: #equal
                return currentNode, parentNode, isChildRight
        return None,None,None
    
    def _updateVal(self, thisNode,parentNode,isChildRight):
        if(isChildRight==True):parentNode.right = thisNode
        elif(isChildRight==False):parentNode.left = thisNode
        else:self.root = thisNode
    
    def remove(self, value):
        thisNode,parentNode,isChildRight = self._lookupWithParent(value) #find V
        #check
        if(thisNode == None):
            return "the item is not exist"
        #   val
        #  /   \
        #none   none
        if(thisNode.right == None and 
        thisNode.left == None):#is V leaf
            self._updateVal(None,parentNode,isChildRight)
            return "is V leaf"
        #   val
        #  /   \
        #none   x
        elif(thisNode.right != None and 
        thisNode.left == None):#is V has one child(right)
            self._updateVal(thisNode.right,parentNode,isChildRight)
            return "is V has one child(right)"
        #  val
        #  / \ 
        # x   None
        elif(thisNode.right == None and 
        thisNode.left != None):#is V has one child(left)
            self._updateVal(thisNode.left,parentNode,isChildRight)
            return "is V has one child(left)"
        #  val
        #  / \
        # x   x
        else:#replace with successor
            #  val
            #  / \
            # x   x
            #    /
            #   none
            if(thisNode.right != None and thisNode.right.left == None):
                thisNode.right.left = thisNode.left
                self._updateVal(thisNode.right,parentNode,isChildRight)
                return "replace with successor(1)"
            #   val
            #  /   \
            # x     x
            #      /
            #      x
            #     ...
            else:
                successorParent = thisNode.right
                successor = thisNode.right.left
                while(successor.left != None):
                    successorParent = successor
                    successor = successor.left
                successorParent.left = successor.right
                
                successor.left = thisNode.left
                successor.right = thisNode.right
                
                self._updateVal(successor,parentNode,isChildRight)
                return "replace with successor(2)"
    
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
    #Inorder Traversal (We get sorted order of elements in tree)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)
        
                







myBST = BinarySearchTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
myBST.insert(160)
myBST.insert(190)
myBST.insert(165)

print("#remove",myBST.remove(9))
print("#printTree")
myBST.print_tree()
print("#root",myBST.root.value)


#     9
#  4    20
# 1 6 15 170
#       160 190
#        165

# print("#printTree_homemade")
# print(myBST.root.value)
# print(myBST.root.left.value)
# print(myBST.root.right.value)

# print(myBST.root.left.left.value)
# print(myBST.root.left.right.value)
# print(myBST.root.right.left.value)
# print(myBST.root.right.right.value)

