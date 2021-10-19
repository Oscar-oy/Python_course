'''
My first solution
'''
'''0
def anagram(s1,s2):
    s4 = []
    s3 = []
    t = True
    for char1 in s2:
        s4.append(char1)
    for char in s1:
        if char in s4 and char != " ":
            s4.remove(char)
            print(s4)
        else:
            if char != " ":
                t = False
                break
        print(t)
    if s4.count(" ") != len(s4):
        t = False
    return t
'''

'''
ANOTHER SOLUTION
This is maybe the best but if the want to ask us about
arrays, maybe is not the optimal way and we 
should implement a manual way
'''
'''
def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)
'''

'''
Best solution in an Interview
'''

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #Edge case check
    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
    return True

s1 = "public relationsxxxxxxx"
s2 = "crap built on lies"
print(anagram(s1,s2))

'''
Now we use a test to check it
'''

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print ("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
