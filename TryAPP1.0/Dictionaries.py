'''
A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.)
instead of using its index to address it.

For example, a database of phone numbers could be stored using a dictionary like this:
'''

phonebook = {}
phonebook["John"]=7251866746
phonebook["Jack"]=8570958292
phonebook["Jill"]=9896015392

print(phonebook)

# another way to declare the dictionaries
phonebook = {
    "John" : 938477566,
    "Jack2" : 938377264,
    "fuddu" : 947662781
}
print(phonebook)

#Iterating over dictionaries

