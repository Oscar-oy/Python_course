#PROBLEM 3
'''
Note, this is a more advanced problem than the previous two! It aso has a lot of variation possibilities and we're ignoring strict requirements here.

Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']
'''

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