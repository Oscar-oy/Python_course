#PROBLEM 3
'''
Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're ignoring strict requirements here.

Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']
'''
#My solution
def word_split(phrase,list_of_words,output=None):
    palabra = ""
    if output is None:
        output = []
    for i in phrase:
        palabra = palabra+i
        phrase = phrase[1:]
        if palabra in list_of_words:
            output.append(palabra)
            return word_split(phrase,list_of_words,output)

    return output

print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split('themanran',['clown','ran','man']))

#Course solution
def word_split1(phrase,list_of_words,output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 

    #Checks to see if any output has been initiated
    #If you default output = [], it would be overwritten for every recursion
    if output is None:
        output = []

    #For every word in list
    for word in list_of_words:
        #If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):

            #Add the word to the output
            output.append(word)

            #Recursively call the split function on the remaining portion of the phrase[len(word)]
            return word_split(phrase[len(word):],list_of_words,output)

    #Finaly return output if no phrase.startswith(word) returns True
    return output

print(word_split1('themanran',['the','ran','man']))
print(word_split1('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split1('themanran',['clown','ran','man']))
