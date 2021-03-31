class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
        """ex
        {0:[1,2],
        1:[2,5,0]...}
        """
    
    def addVertex(self, node):
        self.numberOfNodes += 1
        self.adjacentList[node] = []
    
    def addEdge(self,node1,node2):
        #undirected Graphs
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        
    
    def showConnections(self):
        for key in  self.adjacentList:
            print(key,"-->", self.adjacentList[key])

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')

myGraph.addEdge('3','1')
myGraph.addEdge('3','4')
myGraph.addEdge('4','5')
myGraph.addEdge('4','2')
myGraph.addEdge('5','6')
myGraph.addEdge('2','1')
myGraph.addEdge('0','1')
myGraph.addEdge('2','0')

myGraph.showConnections()
# print(myGraph.adjacentList)
# print(myGraph.numberOfNodes)

"""Answer:
0-->1,2
1-->0,2,3
2-->0,1,4
3-->1,4
4-->2,3,5
5-->4,6
6-->5
"""
# 3 - 4 - 5
# |   |   |
# 1 - 2   6
#  \ /
#   0

    