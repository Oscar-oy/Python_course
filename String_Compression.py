'''
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

#My solution

import collections

def compress(s):
    d = collections.defaultdict(int)
    sol = []
    for letter in s:
        d[letter] +=1
        if letter  not in sol:
            sol.append(letter)
    i = 0
    while i < len(sol):
        sol[i]= sol[i]+str(d[sol[i]])
        i+=1
    sol = "".join(sol)
    return sol


print(compress('AAAAABBBBCCCC'))





"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)