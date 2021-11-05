class BinaryTree(object):

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
r.insertLeft('b')
r.insertLeft('c')
r.insertLeft('d')
r.insertLeft('e')
r.getLeftChild().insertRight('f')
r.getLeftChild().getRightChild().insertLeft('g')
r.getLeftChild().getRightChild().insertRight('h')
r.insertRight('i')
r.insertRight('j')
r.getRightChild().insertLeft('k')
r.getRightChild

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

print('using preorder')
preorder(r)

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

print('using postorder')
postorder(r)

'''
                       a
                    /     \
                    e      j
                  /  \     /\ 
                 d    f   k  i
                /     /\
               c     g  h
              /
             b   

'''
print('using inorder')

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        

inorder(r)