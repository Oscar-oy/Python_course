'''
Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''
'''
#My solution
def uni_char(s):
    sol = []
    length = len(s)
    i = 0

    if length == 0 or length==1:
        return True
    while i < length:
        if s[i] not in sol:
            sol.append(s[i])
        else:
            return False

        i+=1
    return True
'''

#Course solutions
def uni_char(s):
    return len(set(s)) == len(s)

def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)

    return True









"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)