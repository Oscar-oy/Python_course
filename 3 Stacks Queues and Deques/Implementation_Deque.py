class Deque():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items==[]

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.size())

print(d.removeFront()+' '+d.removerear())
print(d.isEmpty())
