#My solution

def pair_sum(arr,k):
    arr = sorted(arr)
    cont = 0
    cont2 = 0
    for num in arr:
        t = k - num
        if t in arr and arr.index(t)<cont2:
            cont += 1
            print((t,num))
        cont2 +=1
    return cont
            
arr = [1,3,2,2]
k = 4
pair_sum(arr,k)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print ('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)
    