class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}


    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+ ' connected to: '+str([x.id for x in self.connectedTo])

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

    def addVertex(self,key):
        self.numVertices = self.numVertices +1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




    # Now we can build the Graph to do a Word Ladder

    def buildGraph(wordFile):
        d = {}
        g = Graph()

        wfile = open(wordFile,'r')
        # create buckets of words that deffer by one letter
        for line in wfile:
            print(line)
            word = line[:-1]
            print(word)
            for i in range(len(word)):
                bucket = word[:i]+ '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

        # add vertices and edges for words in the same bucket

        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1,word2)

        return g

    

    

