#PROBLEM 2
'''
Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1
# You'll neeed to use modulo
4321%10
4321 / 10
'''
#My solution
#print(3%10)
def sum_func(n):

    if not n<10:

        return int(n%10)+sum_func(n/10)

    return int(n%10)
    

print(sum_func(4321))

#Course solution
def sum_func1(n):
    #Base case
    if len(str(n)) == 1:
        return n
    else:
        return int(n%10)+sum_func1(int(n/10))

print(sum_func1(4321))