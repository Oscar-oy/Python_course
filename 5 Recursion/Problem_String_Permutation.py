#String Permutation
'''
Problem Statement
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
'''
#Course solution
def permute(s):
    out = []

    #Base case
    if len(s)==1:
        out = [s]
    
    else:

        #for every letter in string

        for i,let in enumerate(s):

            #for every permutation resulting from step 2 and 3
            print(s)
            print ('first part: ',s[:i],'Second part:',s[i+1:])

            for perm in permute(s[:i]+s[i+1:]):
                print('current letter ',i,', ', let)
                print('perm is ',perm)

                # Add it to output
                out += [let+perm]

    return out

    '''
    En esta función está cogiendo la letra que quiere
    ver las permutaciones y menda el resto a la función de nuevo
    Para que las permutaciones resultanmtes del resto de letras 
    las pueda unir a la solución con la letra inicial delante.
    '''


print(permute('abc'))