
class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.value)
print(a.nextnode)
print(a.nextnode.value)

'''
PROS
-> Linked Lists have constant-time insertions and 
   delections in any position, in comparison, arrays
   require O(n) time to do the same

-> Linked list can continue to expand without having
   to specify their size ahead of time.

CONS
-> To access an element in a linked list, you need to
   take O(k) time to go from the head of the list to the
   kth element. In contrast, arrays have constant time
   operations to access elements in an array

'''
