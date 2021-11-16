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


# Course solution

# This is a basic recursion solution which is not efficient 
# And we could have some problems with weird numbers
def rec_coin1(target,coins):

    # DEFAULT VALUE SET TO TARGET
    min_coins = target

    # CHECKS TO SEE IF TARGET IN IN COINS VALUE LIST
    if target in coins:
        return 1

    else:
        # For every coin value that is <= my target
        for i in [c for c in coins if c<=target]:

            #ADD A COIN COUNT + RECURSIVE CALL
            num_coins = 1 + rec_coin(target-i,coins)

            # RESET MINIMUM IF THE NEW NUM_COINS LESS THAN MIN_COINS
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

print(rec_coin1(63,[1,5,10,25]))

# We should use memoization

# Dynamicly
def rec_coin_dynam(target,coins,know_results):

    # Default output to target
    min_coins = target

    #Base Case
    if target in coins:
        know_results[target] = 1
        return 1
    # Return a known resurl if it happens to be grater than 1
    elif know_results[target]>0:
        return know_results[target]

    else:

        #For every coin value that is <=target
        for i in [c for c in coins if c<= target]:

            num_coins = 1 +rec_coin_dynam(target-i,coins,know_results)

            if num_coins < min_coins:

                min_coins = num_coins

                # Reset that known results
                know_results[target] = min_coins

    return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

print(rec_coin_dynam(target,coins,known_results))




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