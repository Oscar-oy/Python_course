'''
In this script we are going to see some examples
about Big-0 functions
'''
lst=[1,2,3,4,5]
#O(1) constant
def func_constant(lst):
    #prints first item in a list of values
    print(lst[0])
func_constant(lst)

#O(n)Linear
def func_lin(lst):
    #Takes in list and prints out all values
    for val in lst:
        print(val)
func_lin(lst)

#O(n^2) Quadratic
def func_quad(lst):
    #Prints pairs for every item in list
    for item_1 in lst:
        for item_2 in lst:
            print(item_1,item_2)
func_quad(lst)

#Now we are going to see more examples

def print_2(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
print_2(lst)
'''
We can see that this function just grow linear
like O(2n) but 2 is a constant then that's a linear
function as well
'''

def comp(lst):
    print(lst[0]) #O(1)

    midpoint = int(len(lst)/2)

    for val in lst[:midpoint]: #O(n/2)
        print(val)

    for x in range(10): #O(10)
        print('Hello world')

comp(lst)
'''
We can see that this function hace a constant
a linear function and anotre constant
O(1+n/2+10) -> O(1/2*n+11) -> O(n)
finaly this is like a linar function
'''

def matcher(lst,match):
    for item in lst:
        if item == match:
            return True
    return False

print(matcher(lst,1))
'''
This is the best case O(1)
'''
print(matcher(lst,11))
'''
This is worst case
'''

'''
We should consider worst case but we should 
make a point in the best case
'''


# Now we can see it acording to the space that the function is taking

def create_list(n):
    new_list= []

    for num in range(n):
        new_list.append("new")
    return new_list

print(create_list(5))

'''
The space of the list scale with the n 
'''
def printer(n):
    for x in range (n):
        print('hello world')

printer(10)
'''
This function is just saving 1 hello world and
printing it n times.
Time complexity is O(n)
Space Complexity is O(1) 
'''
