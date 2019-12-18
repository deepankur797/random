'''
In this file you will see various string function

'''
astring="Hello WorLd!"
#length function
print(len(astring))

#index for very first element found
print(astring.index("o"))

#finding count of a letter
print(astring.count("l"))
print(astring.count("L"))

#print the substing 3 included 7 excluded
print(astring[3:7])
print(astring[-2]) # single digit from back
print(astring[-2:]) #from given to the end of sentence

#This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].
print(astring[3:7:2])
print(astring[3:7:1])

#There is no function like strrev in C to reverse a string.
#But with the above mentioned type of slice syntax you can easily reverse a string like this

print(astring[::-1])

#These make a new string with all letters converted to uppercase and lowercase, respectively.
print(astring.upper())
print(astring.lower())

#Following is used to determine whether the string starts with something or ends with something, respectively.
# The first one will print True, as the string starts with "Hello". The second one will print False,
#  as the string certainly does not end with "asdfasdfasdf".

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)

 