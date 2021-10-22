'''
Implement a Queue - Using Two Stacks
Given the Stack class below, implement a Queue class using two stacks! Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.
'''
#My solution
class Queue2Stacks(object):
    def __init__(self):
        #two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)

    def dequeue(self):
        l = len(self.stack1)
        for i in range(l):
            self.stack2.append(self.stack1.pop())
        s = self.stack2.pop()
        l = len(self.stack2)
        for i in range(l):
            self.stack1.append(self.stack2.pop())

        return s

"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print( q.dequeue())