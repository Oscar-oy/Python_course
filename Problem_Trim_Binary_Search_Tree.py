# Trim a Binary Search Tree

'''
Problem Statement
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:

and we’re given min value as 5 and max value as 13, then the resulting binary search tree should be:

We should remove all the nodes whose value is not between min and max.
'''



def trimBST(tree,minVal,maxVal):
    
     tree.left # LeftChild
     tree.right # Right Child
     tree.val # Node's value
     
     if tree.left:
        if tree.left.val < minVal:
            tree.left = tree.left.right

        elif tree.left.val > maxVal:
            tree.left = tree.left.left
            
        if tree.left:
            trimBST(tree.left,minVal,maxVal)

     if tree.right:
         if tree.right.val > maxVal:
             tree.right = tree.right.left

         elif tree.right.val < minVal:
             tree.right = tree.right.right
         if tree.right:
            trimBST(tree.right,minVal,maxVal)







'''
following code is just to check if it's working properly
'''

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 
import collections

from Binary_Search_Tree_Implementation import TreeNode
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


   


tree = Node(8)
tree.left = Node(3)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.left.right.left = Node(4)
tree.left.right.right = Node(7)
tree.right = Node(10)
tree.right.right = Node(14)
tree.right.right.left = Node(13)
levelOrderPrint(tree)
trimBST(tree,5,13)
levelOrderPrint(tree)
