'''
Example about private and public methods
'''

class M(object):
    def public(self):
        print("use Tab to see me!")

    def _private(self):
        print("You won't be able to tab see me")

m=M()
m.public()
m._private()

'''
we are going to create our self Dinamy Array
'''
import ctypes
import sys

class DynamicArray(object):
    '''
    DYNAMIC ARRAY (Similar to Python List)
    '''
    def __init__(self):
        self.n = 0 #count actual elements
        self.capacity = 1 #Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n
    def cap(self):
        """
        Return number of elements sorted in array
        """
        return self.capacity

    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!')
        #Check it k index is in 
        return self.A[k] #Retrieve from array at index k

    def append(self,ele):
        '''
        Add element to end of the array
        '''
        if self.n == self.capacity:
            self._resize(2*self.capacity)#Double capacity if not enough room
        
        self.A[self.n] = ele #Set self.n index element
        self.n +=1

    def _resize(self,new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap) #New bigger array

        for k in range(self.n): #Reference all existing values
            B[k] = self.A[k]

        self.A = B #call A the new bigger array
        self.capacity = new_cap #Reset the capacity

    def make_array(self,new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

#Instantiate
arr=DynamicArray()
#Append new element
arr.append(1)
#Check length
print(len(arr))
#Append new element
arr.append(2)
#Check length
print(len(arr))
#Index
print(arr[0])
print(arr[1])
print(arr[3])

'''
Testing auto-resizes
'''

# Set n

n = 10
#data = DynamicArray()
data = DynamicArray()
for i in range(n):
    #Number of elements
    a = len(data)

    #Actual size in Bytes
    b=sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))

    #increase Length by one
    data.append(i)
    print(data[i])
    print(data.cap())
