# Fibonnaci Sequence
'''
Problem Statement
Implement a Fibonnaci Sequence in three different ways:

Recursively
Dynamically (Using Memoization to store results)
Iteratively
Function Output
Your function will accept a number n and return the nth number of the fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).
'''

# My solution


# Recursively
def fib_rec(n):
    if n == 0:
        return 0

    if 0<n<2:
        return 1

    return fib_rec(n-1)+fib_rec(n-2)


print(fib_rec(10))

# Dynamically

# Instantiate Cache information

'''
This is the way to pass all tests becase we have to
reset cache for all tests
'''
def fib_dyn(n):
    cache = [None] * (n + 1)
    def dyn(n):

        if n == 0:
            return 0

        if 0<n<2:
            return 1
        if cache[n]==None:
            cache[n] = dyn(n-2)+dyn(n-1)
        return cache[n]
    return dyn(n)

print(fib_dyn(10))


# Iteratively

def fib_iter(n):
    b1 = 0
    b2 = 1
    sol = 1
    if n == 0:
        return 0
    
    for i in range(n-1):
        sol = b1+b2
        b1 = b2
        b2 = sol

    return sol

print(fib_iter(23))





# Course solution

def fib_iter(n):
    # Set starting point
    a,b= 0,1

    # Follow algorithm
    for i in range(n):

        a,b = b,a+b

    return a

def fib_rec(n):
    # Base case
    if n ==0 or n==1:
        return n
    # Recursive Case
    else:
        return fib_rec(n-1)+fib_rec(n-2)

n = 10
cache = [None]*(n+1)

def fib_dyn(n):
    # Base case
    if n ==0 or n==1:
        return n

    # Check Cache
    if cache[n] != None:
        return cache[n]

    # Keep Setting Cache
    cache[n] = fib_dyn(n-1)+fib_dyn(n-2)

    return cache[n]


"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print ('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

#t.test(fib_rec)
t.test(fib_dyn) # Note, will need to reset cache size for each test!
#t.test(fib_iter)