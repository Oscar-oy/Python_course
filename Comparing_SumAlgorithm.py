#We will compare 2 Algorithm to see who is faster
import time
def sum1(n):
    #take an input of n and return the sum of the numbers from 0 to n

    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return final_sum
print (sum1(10))

def sum2(n):
    #take an input of n and return the sum of the numbers from 0 to n
    return (n*(n+1))/2
print (sum2(10))
'''
this is a function that I created to see time because he was using Ipython
maybe it's not the best but is just a way to compare it
'''
def look_time(n):
    start= time.time()
    n
    time.sleep(1)
    print( time.time() -1- start)
look_time(sum1(100))
look_time(sum2(100))
