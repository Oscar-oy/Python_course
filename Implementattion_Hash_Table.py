#Implementation of a Hash Table

'''
Map
The idea of a dictionary used as a hash table to get and retrieve items using keys is often referred to as a mapping. In our implementation we will have the following methods:

HashTable() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored
in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.

'''


class HashTable(object):

    def __init__(self,size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):

        hashvalue = self.hasfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue]= key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue]= data

            else:
                nextslot = self.rehash(hashvalue,len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data

        

    def hasfunction(self,key,size):
        #The actual hash function

        return key%size
        
    def rehash(self,oldhash,size):

        return (oldhash+1)%size

    def get(self,key):

        startslot = self.hasfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:

                position = self.rehash(position,len(self.slots))

                if position == startslot:

                    stop = True

        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        return self.put(key,data)



h = HashTable(5)

h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
print(h[1])
print(h[2])
print(h[3])
h[13] = 'hi'
h[6] = 'ho'

print(13%5)
print(h[4])
print(h[3])
print(h[5])
print(h[2])
print(h[1])
print(h[13])
print(h[0])
'''
diferent calls to see how it works
'''

