'''
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
'''
'''
#My solution

def rev_word(s):
    s= s.split()
    i = len(s)-1
    sol=[]
    while i >= 0:
        sol.append(s[i])
        i-=1
    return " ".join(sol)

'''

#Course solution using python habilities
def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])


def rev_word(s):
    words= []
    length = len(s)
    spaces = [' ']
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1
    return " ".join(reversed(words))


print(rev_word('Hi John,   are you ready to go?'))
print(rev_word('    space before'))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)