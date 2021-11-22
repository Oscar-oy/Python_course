# Implementation of a Graph as an Acjacency List



class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)+' connectedTo: '+ str([x.id for x in self.connectedTo])


    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,vert):
        self.numVertices += 1
        newVert = Vertex(vert)

        self.vertList[vert] = newVert
        return newVert

    def addEdge(self,fromVert,toVert,weight = 0):

        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert)

        if toVert not in self.vertList:
            nv = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight)


    def getVertex(self,key):

        if key in self.vertList:
            return self.vertList[key]

        else:
            return None

    def getVertices(self):

        return self.vertList.keys()

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

