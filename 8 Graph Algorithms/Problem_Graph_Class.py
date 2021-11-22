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


# Now we gonna implement graph Class with Node class

from enum import Enum

class State(Enum):
    unvisited = 1 #white
    visited = 2 #Black
    visiting = 3 #Gray

from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict() #key = node, val = weight

    def __str__(self):
        return str(self.num)


class GraphN:

    def __init__(self):
        self.nodes = OrderedDict() #key = node id, val = node

    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self,source,dest,weight = 0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight

g = GraphN()
g.add_edge(0, 14, 5)
g.add_edge(0, 3, 5)
print(g.nodes)
g.add_edge(3, 6, 5)
print(g.nodes)