class Vertex :
    """docstring for Vertex"""
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def addNeightbor(self,nbr,weight=0):
        #nbr:Vertex.id
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])
        # return str(self.id)
    def getConnections(self):
        return self.connectedTo.keys()    
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]  
    # def __iter__(self):
    #     return iter(self.connectedTo.values())      

class Graph :
    def __init__(self):
        self.vertList = {}
        self.countVert = 0
    def addVertex(self,key):
        self.countVert += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            None
    def __contains__(self,k):
        return k in self.vertList
    def addEdge(self,start,end,cost=0):
        if start not in self.vertList:
            self.addVertex(start)
        if end not in self.vertList:
            self.addVertex(end)
        self.vertList[start].addNeightbor(self.vertList[end],cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
if __name__ == '__main__':
    graph = Graph()
    for x in range(6):
        graph.addVertex(x)
    for v in graph:
        print(v) 
    print(graph.vertList)
    graph.addEdge(0,1,5)
    graph.addEdge(0,5,2) 
    graph.addEdge(1,2,4)  
    graph.addEdge(2,3,9)
    graph.addEdge(3,4,7)
    graph.addEdge(3,5,3)
    graph.addEdge(4,0,1)
    graph.addEdge(5,4,8)
    graph.addEdge(5,2,1)
    for v in graph:     
        for x in v.getConnections():
            print("(%s,%s)"%(v.getId(),x.getId()))
    for v in graph:
        print(v)
    print(graph.getVertices())
        