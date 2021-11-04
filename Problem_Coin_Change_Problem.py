# Coin Change Problem

'''

Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.
'''


# My solution

def rec_coin(target,coins):
    
    sol = []
    rest = target
    long = target
    coins = sorted(coins,reverse=True)
    for num in coins:
        while num <= rest:
            sol.append(num)
            rest = rest - num
        long = min(len(sol),rec_coin(target,coins[1:]))
    return long
    

print(rec_coin(10,[1,5]))



"""
RUN THIS CELL TO TEST YOUR FUNCTION.
NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION 
      GO CHECK THE SOLUTION NOTEBOOK INSTEAD OF RUNNING THIS!
"""

from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        print ('Passed all tests.')
# Run Test

test = TestCoins()
test.check(rec_coin)