# Tree Level Order Print
'''
Given a binary tree of integers, print it in level order. The output will contain space between the numbers in the same level, and new line between different levels. For example, if the tree is:


The output should be:

1 
2 3 
4 5 6
'''

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 
import collections
def levelOrderPrint(tree):
    
    if not tree:
        return

    nodes = collections.deque([tree])

    currentCount = 1
    nextCount = 0

    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        
        print(currentNode.val)

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount +=1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        
        if currentCount == 0:
            print('\n')
            currentCount,nextCount = nextCount,currentCount


   

'''
We should notice that we are using postorder traversal to read the tree
'''

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.left = Node(5)
tree.right.right = Node(6)
tree.left.left.right = Node(7)
levelOrderPrint(tree)


