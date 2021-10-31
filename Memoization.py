
'''
We are using the factorial problem like an example of memoization
'''



#Create cache for known results
factorial_memo = {}
def factorial(k):
    if k <2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k]=k*factorial(k-1)
    return factorial_memo[k]

print(factorial(4))
#We are now able to increase the efficiency of this function by remembering old results!

'''
We can also encapsulate the memoization process into a class:
'''


class Memoize:
    def __init__(self,f):
        self.f = f
        self.memo = {}
    def __call__(self,*args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def factorial(k):
    if k<2:
        return 1
    return k*factorial(k-1)


factorial = Memoize(factorial)


