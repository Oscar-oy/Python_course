'''
Problem
Given an array of integers (positive and negative) find the largest continuous sum.
'''
'''
#My solution

def large_cont_sum(arr):
    index = 0
    sol = 0
    t = True
    while t:
        t = False
        i = index
        index = 0
        suma = 0
        while i < len(arr):
            suma += arr[i]
            if suma > sol:
                sol = suma
                print(sol)
            if arr[i] < 0 and index == 0:
                print('estoy aqui')
                index = i+1
                if index <= len(arr)-1:
                    t =True
            i+=1
        print (t)
                
    return sol
'''

#Course solution
def large_cont_sum(arr):

    if len(arr)==0:
        return 0 
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum,max_sum)
    return max_sum







print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
#print(large_cont_sum([-1,1]))
print(large_cont_sum([3,1,-1,-12,20,1,-12]))


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)