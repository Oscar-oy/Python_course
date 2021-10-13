'''
This is just an example of doing our own test
necessary to install nose: pip install nose
Then you should choose the interpreter where packets were installed: F1 -> select interpreter
'''

def solution (num1,num2):
    return num1+num2

from nose.tools import assert_equal

# We define a class
class SolutionTest(object):

    def test(self,sol):
        assert_equal(sol(2,2),4)
        assert_equal(sol(4,4),8)
        

        print("ALL TEST CASES PASSED")


# Run Test
t=SolutionTest()
t.test(solution)
